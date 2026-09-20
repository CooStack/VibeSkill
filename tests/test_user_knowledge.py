import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import user_knowledge as knowledge


class UserKnowledgeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.root = self.base / "personal"
        self.project = self.base / "project-a"
        self.project.mkdir()
        self.other = self.base / "project-b"
        self.other.mkdir()
        self.environment = patch.dict(os.environ, {
            "VIBESKILL_KNOWLEDGE_HOME": str(self.root),
            "USERPROFILE": str(self.base / "home"),
            "HOME": str(self.base / "home"),
            "LOCALAPPDATA": str(self.base / "unused-appdata"),
            "XDG_DATA_HOME": str(self.base / "unused-xdg"),
            "PYTHONDONTWRITEBYTECODE": "1",
        })
        self.environment.start()
        self.addCleanup(self.environment.stop)
        self.data = {"title": "Heavy swing", "definition": "A user-defined sound target."}

    def save(self, payload=None, **kwargs):
        return knowledge.save_concept(
            self.data if payload is None else payload, project=self.project, **kwargs)

    def cli(self, *args, data=None):
        return subprocess.run(
            [sys.executable, "-B", str(ROOT / "scripts" / "learn_concept.py"), *args],
            input=data, text=True, encoding="utf-8", capture_output=True,
            cwd=self.project, env=dict(os.environ), timeout=15,
        )

    def catalog(self):
        return json.loads((self.root / "concepts.json").read_text(encoding="utf-8"))

    def test_root_override_and_home_defaults_without_creating(self):
        self.assertEqual(knowledge.knowledge_root(), self.root)
        with patch.dict(os.environ, {"VIBESKILL_KNOWLEDGE_HOME": ""}):
            with patch.object(knowledge.sys, "platform", "win32"):
                self.assertEqual(knowledge.knowledge_root(), self.base / "home" / "VibeSkill")
            with patch.object(knowledge.sys, "platform", "linux"):
                with patch.object(Path, "home", return_value=self.base / "unix-home"):
                    self.assertEqual(knowledge.knowledge_root(), self.base / "unix-home" / "VibeSkill")
        self.assertFalse(self.root.exists())
        self.assertFalse((self.base / "unused-appdata").exists())
        self.assertFalse((self.base / "unused-xdg").exists())

    def test_empty_load_is_readonly_and_init_is_idempotent(self):
        self.assertEqual(knowledge.load_user_concepts(project=self.project), [])
        self.assertFalse(self.root.exists())
        self.assertEqual(knowledge.initialize_knowledge(), self.root)
        self.assertEqual(knowledge.initialize_knowledge(), self.root)
        self.assertTrue((self.root / "index.md").is_file())
        self.assertEqual(self.catalog(), {"version": 1, "concepts": []})

    def test_personal_store_cannot_be_created_inside_public_skill(self):
        for path in (ROOT, ROOT / "private-data"):
            with self.subTest(path=path), self.assertRaisesRegex(ValueError, "outside the Skill"):
                knowledge.save_concept(self.data, root=path, project=self.project)

    def test_git_root_and_descendant_are_rejected_without_overwriting(self):
        repository = self.base / "other-repository"
        (repository / ".git").mkdir(parents=True)
        index = repository / "index.md"
        index.write_text("User-owned document", encoding="utf-8")
        for root in (repository, repository / "nested-store"):
            with self.subTest(root=root), self.assertRaisesRegex(ValueError, "Git working tree"):
                knowledge.save_concept(self.data, root=root, project=self.project)
            self.assertFalse((root / "concepts.json").exists())
        self.assertEqual(index.read_text(encoding="utf-8"), "User-owned document")

    def test_existing_unowned_index_is_not_overwritten(self):
        self.root.mkdir()
        index = self.root / "index.md"
        index.write_text("Existing notes", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unrelated data"):
            knowledge.initialize_knowledge()
        self.assertEqual(index.read_text(encoding="utf-8"), "Existing notes")
        self.assertFalse((self.root / "concepts.json").exists())
        self.assertFalse((self.root / ".knowledge.lock").exists())

    def test_transient_windows_read_sharing_denial_is_retried(self):
        original = knowledge.os.replace
        attempts = []
        error = PermissionError("Sharing violation")
        error.winerror = 32
        def replace(source, destination):
            attempts.append(destination)
            if len(attempts) == 1:
                raise error
            return original(source, destination)
        with patch.object(knowledge.os, "replace", side_effect=replace):
            record = self.save()
        self.assertEqual(knowledge.get_user_concept(record["id"], project=self.project), record)
        self.assertGreater(len(attempts), 1)

    def test_persistent_windows_denial_preserves_existing_catalog(self):
        record = self.save()
        before = (self.root / "concepts.json").read_bytes()
        error = PermissionError("Access denied")
        error.winerror = 5
        with patch.object(knowledge, "REPLACE_RETRY_SECONDS", 0):
            with patch.object(knowledge.os, "replace", side_effect=error):
                with self.assertRaises(PermissionError):
                    self.save({"definition": "Must not commit"}, update_id=record["id"])
        self.assertEqual((self.root / "concepts.json").read_bytes(), before)

    def test_record_contract_and_readable_absolute_links(self):
        record = self.save({"title": "Custom / Sound", "definition": "Meaning",
                            "aliases": ["Weight"], "domain": "unregistered-domain",
                            "origin": "personal convention", "verification": "user_defined"})
        expected = {
            "id", "domain", "concept", "cues", "meaning", "boundary", "path", "line",
            "reader_path", "reader_link", "personal", "origin", "scope", "project",
            "verification", "sources",
        }
        self.assertEqual(set(record), expected)
        self.assertRegex(record["id"], r"^UK-[0-9a-f]{32}$")
        self.assertEqual(record["concept"], "Custom / Sound; Weight")
        self.assertTrue(record["personal"])
        self.assertEqual(record["verification"], "user_defined")
        reader = Path(record["reader_path"])
        self.assertTrue(reader.is_file())
        self.assertTrue(reader.is_relative_to(self.root))
        self.assertIn(reader.as_posix(), record["reader_link"])
        index = (self.root / "index.md").read_text(encoding="utf-8")
        self.assertIn(f"(readers/{record['id']}.md)", index)
        self.assertNotIn(self.root.as_posix(), index)
        self.assertEqual(knowledge.get_user_concept(record["id"], project=self.project), record)

    def test_idempotence_normalization_preserves_original(self):
        first = self.save()
        second = self.save({"title": "  HEAVY   swing ", "definition": "Must not overwrite"})
        self.assertEqual(first, second)
        self.assertEqual(len(self.catalog()["concepts"]), 1)
        fullwidth = "\uff28\uff45\uff41\uff56\uff59 swing"
        self.assertEqual(self.save({"title": fullwidth, "definition": "Other"})["id"], first["id"])

    def test_cli_utf8_stdin_ignores_host_stream_encoding(self):
        payload = {"title": "星印", "definition": "三份素材构成的自定义提示。"}
        with patch.dict(os.environ, {"PYTHONIOENCODING": "ascii"}):
            created = self.cli("--stdin", data=json.dumps(payload, ensure_ascii=False))
        self.assertEqual(created.returncode, 0, created.stderr)
        record = json.loads(created.stdout)
        self.assertEqual(record["meaning"], payload["definition"])
        self.assertEqual(record["concept"], payload["title"])

    def test_partial_update_stable_id_and_identity_assertion(self):
        first = self.save()
        updated = self.save({"definition": "Changed", "identity": first["id"]},
                            update_id=first["id"])
        self.assertEqual(updated["id"], first["id"])
        self.assertEqual(updated["meaning"], "Changed")
        self.assertEqual(updated["concept"], first["concept"])
        self.assertIn("Changed", Path(updated["reader_path"]).read_text(encoding="utf-8"))
        self.assertEqual(self.save({**self.data, "identity": first["id"]}), updated)
        with self.assertRaises(ValueError):
            self.save({**self.data, "identity": "UK-" + "1" * 32})
        with self.assertRaises(KeyError):
            self.save({"definition": "Missing"}, update_id="UK-" + "1" * 32)

    def test_project_isolation_global_visibility_and_cwd_default(self):
        first = self.save()
        other = knowledge.save_concept(self.data, project=self.other)
        global_record = self.save({**self.data, "scope": "global"})
        self.assertEqual(len({first["id"], other["id"], global_record["id"]}), 3)
        visible = knowledge.load_user_concepts(project=self.project)
        self.assertEqual({item["id"] for item in visible}, {first["id"], global_record["id"]})
        with patch.object(Path, "cwd", return_value=self.other):
            self.assertEqual({item["id"] for item in knowledge.load_user_concepts()},
                             {other["id"], global_record["id"]})
        for operation in (knowledge.get_user_concept, knowledge.delete_user_concept):
            with self.assertRaises(KeyError):
                operation(other["id"], project=self.project)
        with self.assertRaises(KeyError):
            self.save({"definition": "Not mine"}, update_id=other["id"])
        self.assertEqual(knowledge.get_user_concept(other["id"], project=self.other), other)

    def test_update_cannot_move_scope_or_collide(self):
        first = self.save()
        self.save({"title": "Other", "definition": "Other"})
        for payload in ({"scope": "global", "project": None},
                        {"project": str(self.other)}, {"title": "Other"},
                        {"identity": "UK-" + "0" * 32}):
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                self.save(payload, update_id=first["id"])
        self.assertEqual(knowledge.get_user_concept(first["id"], project=self.project), first)

    def test_verification_does_not_promote_sources_and_edit_downgrades(self):
        record = self.save({**self.data, "sources": ["https://example.invalid/reference"]})
        self.assertEqual(record["verification"], "unverified")
        checked = self.save({"verification": "source_checked"}, update_id=record["id"])
        self.assertEqual(checked["verification"], "source_checked")
        changed = self.save({"definition": "Unreviewed change"}, update_id=record["id"])
        self.assertEqual(changed["verification"], "unverified")
        self.assertEqual(changed["sources"], record["sources"])

    def test_recipe_schema_and_optional_fallback(self):
        recipe = {"intent": "Meaning", **{key: ["Specific step"] for key in knowledge.RECIPE_LISTS}}
        record = self.save({**self.data, "recipe": recipe})
        self.assertEqual(record["implementation_recipe"], recipe)
        for key in recipe:
            invalid = copy.deepcopy(recipe)
            invalid[key] = [] if key != "intent" else ""
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.save({"recipe": invalid}, update_id=record["id"])
        with self.assertRaises(ValueError):
            self.save({"recipe": {**recipe, "extra": []}}, update_id=record["id"])

    def test_bad_schema_rejected_before_create(self):
        bad = [
            [], {}, {"title": "Only title"}, {**self.data, "aliases": "wrong"},
            {**self.data, "aliases": [False]}, {**self.data, "sources": [3]},
            {**self.data, "verification": "verified"},
            {**self.data, "verification": "source_checked"},
            {**self.data, "scope": "../escape"},
            {**self.data, "scope": "global", "project": str(self.project)},
            {**self.data, "secret": "Do not persist"},
            {**self.data, "raw_chat": "Do not persist"},
            {**self.data, "recipe": None}, {**self.data, "title": "two\nlines"},
        ]
        for payload in bad:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                self.save(payload)
        self.assertFalse(self.root.exists())

    def test_corrupt_catalog_errors_include_path_and_are_not_overwritten(self):
        knowledge.initialize_knowledge()
        path = self.root / "concepts.json"
        for text in ('{broken', '{"version":1,"version":1,"concepts":[]}',
                     '{"version":true,"concepts":[]}',
                     '{"version":1,"concepts":[{}]}', '{"version":NaN,"concepts":[]}'):
            path.write_text(text, encoding="utf-8")
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, "concepts.json"):
                    knowledge.load_user_concepts(project=self.project)
                with self.assertRaisesRegex(ValueError, "concepts.json"):
                    self.save()
                self.assertEqual(path.read_text(encoding="utf-8"), text)
                self.assertFalse((self.root / ".knowledge.lock").exists())

    def test_paths_and_payload_are_data_not_output_paths(self):
        malicious = "../outside <script>bad()</script> [x](file:///secret)"
        record = self.save({"title": malicious,
                            "definition": "```\n<script>bad()</script>\n::directive{}\n```"})
        self.assertEqual(Path(record["reader_path"]).name, record["id"] + ".md")
        for identity in ("../outside", str(self.base), "UK-" + "../" * 12,
                         "UK-" + "A" * 32, "*", ""):
            with self.subTest(identity=identity):
                with self.assertRaises(ValueError):
                    knowledge.delete_user_concept(identity, project=self.project)
                with self.assertRaises(ValueError):
                    self.save({}, update_id=identity)
        page = Path(record["reader_path"]).read_text(encoding="utf-8")
        self.assertIn("````text", page)
        self.assertIn("&lt;script&gt;", page.splitlines()[0])
        self.assertFalse((self.base / "outside").exists())

    def test_internal_symlink_rejected(self):
        self.root.mkdir()
        outside = self.base / "outside"
        outside.mkdir()
        try:
            (self.root / "readers").symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation unavailable on this host")
        with self.assertRaises(ValueError):
            self.save()
        self.assertEqual(list(outside.iterdir()), [])
        self.assertFalse((self.root / "concepts.json").exists())

    def test_delete_only_one_and_nonexistent_is_error(self):
        first = self.save()
        second = self.save({"title": "Keep", "definition": "Keep"})
        result = knowledge.delete_user_concept(first["id"], project=self.project)
        self.assertEqual(result, first)
        self.assertFalse(Path(first["reader_path"]).exists())
        self.assertTrue(Path(second["reader_path"]).is_file())
        self.assertTrue(self.root.is_dir())
        self.assertEqual(knowledge.load_user_concepts(project=self.project), [second])
        self.assertNotIn(first["id"], (self.root / "index.md").read_text(encoding="utf-8"))
        with self.assertRaises(KeyError):
            knowledge.delete_user_concept(first["id"], project=self.project)

    def test_lock_is_exclusive_and_never_stolen(self):
        self.root.mkdir()
        lock = self.root / ".knowledge.lock"
        lock.write_text("external owner", encoding="ascii")
        with self.assertRaises(TimeoutError):
            self.save(lock_timeout=0)
        self.assertEqual(lock.read_text(encoding="ascii"), "external owner")
        self.assertFalse((self.root / "concepts.json").exists())

    def test_parallel_processes_same_and_different_titles(self):
        processes = []
        for title in ("Same", "Same", "Same", "Different"):
            payload = json.dumps({"title": title, "definition": title})
            process = subprocess.Popen(
                [sys.executable, "-B", str(ROOT / "scripts" / "learn_concept.py"), "--stdin"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                text=True, encoding="utf-8", cwd=self.project, env=dict(os.environ))
            processes.append((process, payload))
        records = []
        try:
            for process, payload in processes:
                process.stdin.write(payload)
                process.stdin.close()
                process.stdin = None
            for process, _ in processes:
                stdout, stderr = process.communicate(timeout=15)
                self.assertEqual(process.returncode, 0, stderr)
                records.append(json.loads(stdout))
        finally:
            for process, _ in processes:
                if process.poll() is None:
                    process.kill()
                    process.communicate()
        self.assertEqual(len({record["id"] for record in records[:3]}), 1)
        self.assertEqual(len(knowledge.load_user_concepts(project=self.project)), 2)
        self.assertEqual(list(self.root.rglob("*.tmp")), [])

    def test_cli_complete_crud_and_init_repair(self):
        self.assertEqual(self.cli("--init").returncode, 0)
        path = self.base / "input.json"
        path.write_text(json.dumps(self.data), encoding="utf-8")
        created = self.cli("--file", str(path))
        self.assertEqual(created.returncode, 0, created.stderr)
        record = json.loads(created.stdout)
        fetched = self.cli("--get", record["id"])
        self.assertEqual(json.loads(fetched.stdout), record)
        self.assertEqual(len(json.loads(self.cli("--list").stdout)), 1)
        updated = self.cli("--update", record["id"], "--stdin",
                           data=json.dumps({"definition": "Patched"}))
        self.assertEqual(updated.returncode, 0, updated.stderr)
        self.assertEqual(json.loads(updated.stdout)["id"], record["id"])
        Path(record["reader_path"]).unlink()
        self.assertEqual(self.cli("--init").returncode, 0)
        self.assertTrue(Path(record["reader_path"]).exists())
        deleted = self.cli("--delete", record["id"])
        self.assertEqual(deleted.returncode, 0, deleted.stderr)
        self.assertTrue(json.loads(deleted.stdout)["permanent"])
        self.assertEqual(json.loads(self.cli("--list").stdout), [])
        self.assertEqual(self.cli("--delete", record["id"]).returncode, 2)

    def test_cli_conflicts_and_bad_input_do_not_write(self):
        for args in ((), ("--init", "--list"), ("--update", "UK-" + "0" * 32),
                     ("--list", "--stdin"), ("--get", "x", "--stdin"),
                     ("--delete", "x", "--file", "absent"),
                     ("--stdin", "--file", "absent")):
            with self.subTest(args=args):
                self.assertEqual(self.cli(*args, data="{}").returncode, 2)
        bad = self.cli("--stdin", data='{"title": "x", "secret": "DO_NOT_ECHO"}')
        self.assertEqual(bad.returncode, 2)
        self.assertIn("<stdin>", bad.stderr)
        self.assertNotIn("DO_NOT_ECHO", bad.stderr)
        self.assertFalse(self.root.exists())
        invalid_file = self.base / "broken.json"
        invalid_file.write_text("{oops", encoding="utf-8")
        bad = self.cli("--file", str(invalid_file))
        self.assertIn(str(invalid_file), bad.stderr)
        self.assertEqual(bad.returncode, 2)

    def test_atomic_failure_preserves_catalog(self):
        record = self.save()
        before = (self.root / "concepts.json").read_bytes()
        with patch.object(knowledge.os, "replace", side_effect=OSError("simulated failure")):
            with self.assertRaises(OSError):
                self.save({"definition": "Not committed"}, update_id=record["id"])
        self.assertEqual((self.root / "concepts.json").read_bytes(), before)
        self.assertFalse((self.root / ".knowledge.lock").exists())
        self.assertEqual(list(self.root.rglob("*.tmp")), [])

    def test_derived_view_failure_reports_commit_and_init_repairs(self):
        first = self.save()
        with patch.object(knowledge, "_views", side_effect=OSError("view unavailable")):
            with self.assertRaisesRegex(ValueError, "catalog committed"):
                self.save({"definition": "Committed"}, update_id=first["id"])
        self.assertEqual(knowledge.get_user_concept(first["id"], project=self.project)["meaning"],
                         "Committed")
        knowledge.initialize_knowledge()
        self.assertIn("Committed", Path(first["reader_path"]).read_text(encoding="utf-8"))
        reader_dir = self.root / "readers"
        orphan = reader_dir / ("UK-" + "0" * 32 + ".md")
        manual = reader_dir / "notes.md"
        orphan.write_text("orphan view", encoding="utf-8")
        manual.write_text("keep manual notes", encoding="utf-8")
        knowledge.initialize_knowledge()
        self.assertFalse(orphan.exists())
        self.assertTrue(manual.exists())
        self.assertTrue(Path(first["reader_path"]).exists())

    def test_stored_bad_id_project_and_duplicate_are_rejected(self):
        self.save()
        document = self.catalog()
        path = self.root / "concepts.json"
        cases = []
        for field, value in (("id", "../escape"), ("project", "../project"),
                             ("sources", [None]), ("scope", [])):
            bad = copy.deepcopy(document)
            bad["concepts"][0][field] = value
            cases.append(bad)
        duplicate = copy.deepcopy(document)
        duplicate["concepts"].append(copy.deepcopy(duplicate["concepts"][0]))
        cases.append(duplicate)
        for bad in cases:
            with self.subTest(bad=bad):
                path.write_text(json.dumps(bad), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "concepts.json"):
                    knowledge.load_user_concepts(project=self.project)

    def test_guard_rejects_linked_directory_without_host_symlink_privileges(self):
        self.root.mkdir()
        original = Path.is_symlink
        with patch.object(Path, "is_symlink",
                          lambda path: path == self.root / "readers" or original(path)):
            with self.assertRaisesRegex(ValueError, "linked storage paths"):
                self.save()
        self.assertFalse((self.root / "concepts.json").exists())


if __name__ == "__main__":
    unittest.main()
