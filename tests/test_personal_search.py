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
from search_concepts import (
    load_concepts, load_search_records, load_guidance, load_abbreviations, search,
)
from search_prompt import PromptIndex
from practices import load_practices
from build_library import render_library, load_notes
from user_knowledge import save_concept, delete_user_concept


def personal_record():
    return {
        "id": "UK-0123456789abcdef0123456789abcdef",
        "domain": "user",
        "concept": "星印; StellarMark",
        "cues": "三个素材组合的项目提示",
        "meaning": "本项目把由三个素材组合的提示称为星印。",
        "boundary": "用户自定义，不是密码签名或 token。",
        "path": "personal/concepts/record.json",
        "line": 1,
        "reader_path": "personal/pages/record.md",
        "reader_link": "[星印](personal/pages/record.md)",
        "personal": True,
        "origin": "user_defined",
        "scope": "project",
        "project": str(ROOT),
        "verification": "user_defined",
        "sources": [],
        "implementation_recipe": None,
    }


class PersonalSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.builtins = load_concepts()
        cls.practices = load_practices()
        cls.guidance = load_guidance()
        cls.abbreviations = load_abbreviations()

    def test_catalog_can_exclude_personal_store(self):
        with patch("search_concepts.load_user_concepts", return_value=[personal_record()]) as read:
            all_records = load_search_records(project=ROOT)
            self.assertTrue(all_records[-1]["personal"])
            read.assert_called_once_with(project=ROOT)
        with patch("search_concepts.load_user_concepts", side_effect=AssertionError("must not read")):
            self.assertEqual(load_search_records(include_user=False), self.builtins)

    def test_same_builtin_id_cannot_be_injected(self):
        record = personal_record()
        record["id"] = self.builtins[0]["id"]
        with patch("search_concepts.load_user_concepts", return_value=[record]):
            with self.assertRaises(ValueError):
                load_search_records()

    def test_personal_definition_remains_user_defined(self):
        record = personal_record()
        index = PromptIndex(self.builtins + [record], self.guidance, self.abbreviations, self.practices)
        result = index.search("星印", domain="user")["results"]
        self.assertEqual([item["id"] for item in result], [record["id"]])
        self.assertEqual(result[0]["meaning"], record["meaning"])
        self.assertEqual(result[0]["knowledge_origin"]["verification"], "user_defined")
        self.assertEqual(result[0]["implementation_context"]["specificity"], "definition")
        self.assertEqual(result[0]["status"], "candidate")

    def test_user_filter_includes_personal_entries_in_standard_domains(self):
        record = personal_record()
        record["domain"] = "backend"
        result = search(self.builtins + [record], ["星印"], domain="user")
        self.assertEqual([item["id"] for item in result], [record["id"]])
        index = PromptIndex(self.builtins + [record], self.guidance, self.abbreviations, self.practices)
        row = index.search("星印", domain="backend", limit=1)["results"][0]
        self.assertEqual(row["implementation_context"]["specificity"], "domain")
        self.assertEqual(row["knowledge_origin"]["kind"], "personal")

    def test_personal_recipe_retains_its_origin(self):
        record = personal_record()
        record["implementation_recipe"] = copy.deepcopy(next(iter(self.practices["recipes"].values())))
        index = PromptIndex(self.builtins + [record], self.guidance, self.abbreviations, self.practices)
        row = index.search(record["id"], limit=1)["results"][0]
        self.assertEqual(row["implementation_context"]["specificity"], "personal")
        self.assertEqual(row["knowledge_origin"]["verification"], "user_defined")

    def test_single_character_custom_name_is_retrievable(self):
        record = personal_record()
        record["concept"] = "帧"
        record["meaning"] = "本项目的一次数据库批次。"
        index = PromptIndex(self.builtins + [record], self.guidance, self.abbreviations, self.practices)
        result = index.search("为什么帧会重复", domain="user")["results"]
        self.assertEqual([row["id"] for row in result], [record["id"]])

    def test_generated_builtin_library_does_not_read_personal_store(self):
        with patch("search_concepts.load_user_concepts", side_effect=AssertionError("private data read")):
            pages = render_library(self.builtins, load_notes(), self.abbreviations, self.practices)
        self.assertNotIn("concepts/" + personal_record()["id"] + ".md", pages)

    def test_persisted_concept_is_searchable_then_disappears_after_delete(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            root, project = base / "knowledge", base / "project"
            project.mkdir()
            record = save_concept({
                "title": "UserConceptOnly92741",
                "definition": "Three project-specific items form one custom unit.",
                "verification": "user_defined",
            }, root=root, project=project)
            env = dict(os.environ, VIBESKILL_KNOWLEDGE_HOME=str(root))
            command = [
                sys.executable, "-B", str(ROOT / "scripts" / "search_prompt.py"),
                record["id"], "--limit", "1",
            ]
            def query(*args):
                return subprocess.run(command + list(args), cwd=project, env=env,
                                      capture_output=True, encoding="utf-8", timeout=20)
            result = query()
            self.assertEqual(result.returncode, 0, result.stderr)
            row = json.loads(result.stdout)["results"][0]
            self.assertEqual(row["id"], record["id"])
            self.assertEqual(row["knowledge_origin"]["verification"], "user_defined")
            self.assertTrue(Path(record["reader_path"]).is_file())
            self.assertEqual(query("--builtin-only").returncode, 1)
            self.assertEqual(query("--project", str(base / "other-project")).returncode, 1)
            delete_user_concept(record["id"], root=root, project=project)
            self.assertEqual(query().returncode, 1)


if __name__ == "__main__":
    unittest.main()
