import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "search_concepts.py"
sys.path.insert(0, str(ROOT / "scripts"))
spec = importlib.util.spec_from_file_location("search_concepts", SCRIPT)
search_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(search_module)


class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = search_module.load_concepts()

    def ids(self, queries, **kwargs):
        return [item["id"] for item in search_module.search(self.records, queries, **kwargs)]

    def test_chinese_requirement(self):
        self.assertEqual(self.ids(["重复提交"])[0], "BE008")

    def test_case_and_fullwidth_alias(self):
        self.assertEqual(self.ids(["ｓｓｒ"]), self.ids(["SSR"]))
        self.assertEqual(self.ids(["IDEMPOTENCY"])[0], "BE008")

    def test_ambiguous_acronym(self):
        hits = self.ids(["SSR"])
        self.assertIn("FE013", hits)
        self.assertIn("GM046", hits)
        self.assertNotIn("AR022", hits)

    def test_domain_filter(self):
        hits = self.ids(["SSR"], domain="frontend")
        self.assertEqual(hits, ["FE013"])

    def test_latin_word_boundaries(self):
        self.assertFalse(search_module.contains("building", "ui"))
        self.assertTrue(search_module.contains("UI; 界面", "ui"))

    def test_quoted_phrase(self):
        self.assertEqual(self.ids(["state machine"], domain="frontend")[0], "FE007")

    def test_multiple_terms_rank_shared_match_first(self):
        self.assertEqual(self.ids(["幂等", "重复提交"])[0], "BE008")

    def test_id_lookup(self):
        self.assertEqual(self.ids(["MD036"]), ["MD036"])

    def test_art_and_modeling_are_distinct(self):
        self.assertIn("MD036", self.ids(["蒙皮"]))
        self.assertIn("AR031", self.ids(["遮罩"]))
        self.assertNotIn("MD036", self.ids(["遮罩"], domain="art"))

    def test_unknown_and_limit(self):
        self.assertEqual(self.ids(["__unknown_concept_9384__"]), [])
        self.assertEqual(len(self.ids(["状态"], limit=1)), 1)

    def test_language_and_framework_queries(self):
        scenarios = [
            ("类型擦除", "java", "JV010"),
            ("Generics", "java", "JV010"),
            ("挂起函数", "kotlin", "KT024"),
            ("布尔属性", "html", "HT005"),
            (":has()", "css", "CS004"),
            ("闭包", "javascript", "JS007"),
            ("类型断言", "typescript", "TS015"),
            ("解构后不更新", "vue", "VU006"),
            ("方块实体", "minecraft", "MC022"),
            ("KSP", "tooling", "TL013"),
            ("联合索引", "mysql", "MY013"),
            ("控制反转", "spring", "SP002"),
            ("Verticle", "vertx", "VX003"),
            ("哈希表", "data-structures", "DT008"),
            ("策略模式", "design-patterns", "DP022"),
            ("VAO", "opengl", "GL005"),
            ("软粒子", "graphics", "CG040"),
            ("四元数", "mathematics", "MA013"),
        ]
        for query, domain, expected in scenarios:
            with self.subTest(query=query, domain=domain):
                hits = self.ids([query], domain=domain)
                self.assertTrue(hits)
                self.assertEqual(hits[0], expected)

    def test_every_domain_alias(self):
        for alias, canonical in search_module.DOMAIN_ALIASES.items():
            with self.subTest(alias=alias):
                concept = next(row for row in self.records if row["domain"] == canonical)
                self.assertEqual(self.ids([concept["id"]], domain=alias), [concept["id"]])
                self.assertEqual(
                    self.ids([concept["id"]], domain=alias),
                    self.ids([concept["id"]], domain=canonical),
                )

    def test_java_is_not_javascript(self):
        hits = self.ids(["JavaScript"], domain="java")
        self.assertIn("JV001", hits)
        self.assertNotIn("JS001", hits)
        self.assertFalse(search_module.contains("JavaScript", "java"))

    def test_symbol_queries_are_literal(self):
        self.assertEqual(self.ids(["??"], domain="js")[0], "JS004")
        self.assertEqual(self.ids([":has()"], domain="css")[0], "CS004")
        self.assertEqual(self.ids(["!!"], domain="kt")[0], "KT002")

    def test_minecraft_side_and_loader_queries(self):
        self.assertEqual(self.ids(["Physical side"], domain="mc")[0], "MC012")
        self.assertEqual(self.ids(["Fabric"], domain="mc")[0], "MC004")
        self.assertEqual(self.ids(["Folia"], domain="mc")[0], "MC008")

    def test_vertex_keeps_distinct_meanings(self):
        hits = self.ids(["Vertex"], limit=100)
        self.assertIn("GL003", hits)
        self.assertIn("DT013", hits)
        self.assertIn("VX014", hits)
        self.assertNotIn("vertex", search_module.DOMAIN_ALIASES)
        self.assertEqual(self.ids(["Vert.x"], domain="vertx")[0], "VX001")

    def test_exact_alias_precedes_phrase_match(self):
        hits = self.ids(["Vertex"], domain="opengl")
        self.assertEqual(hits[0], "GL003")
        self.assertIn("GL013", hits)

    def test_cli_markdown_reader_link(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "DP022", "--markdown"],
            capture_output=True, encoding="utf-8"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn((ROOT / "library" / "concepts" / "DP022.md").as_posix(), result.stdout)
        self.assertIn("[", result.stdout)

    def test_cross_reference_ids_exist(self):
        ids = {row["id"] for row in self.records}
        for path in (ROOT / "references").glob("*.md"):
            if path.name == "sources.md":
                continue
            for mention in search_module.ID_PATTERN.finditer(path.read_text(encoding="utf-8")):
                self.assertIn(mention.group(), ids, (path.name, mention.group()))

    def test_sources_and_record_locations(self):
        self.assertEqual(len({row["id"] for row in self.records}), len(self.records))
        self.assertEqual({row["domain"] for row in self.records}, set(search_module.DOMAINS))
        for row in self.records:
            actual_line = Path(row["path"]).read_text(encoding="utf-8").splitlines()[row["line"] - 1]
            self.assertTrue(actual_line.startswith("| " + row["id"] + " |"))

    def test_local_markdown_links(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                self.assertTrue((path.parent / target.split("#")[0]).is_file(), (path, target))

    def test_cli_json_from_different_directory(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "SSR", "--json"],
            cwd=ROOT.parent, capture_output=True, encoding="utf-8"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("FE013", {row["id"] for row in json.loads(result.stdout)})

    def test_cli_no_match(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "__unknown_concept_9384__", "--json"],
            capture_output=True, encoding="utf-8"
        )
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout), [])

    def test_cli_domain_alias(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "方块实体", "--domain", "mc", "--json"],
            cwd=ROOT.parent, capture_output=True, encoding="utf-8"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        records = json.loads(result.stdout)
        self.assertEqual(records[0]["id"], "MC022")
        self.assertEqual({row["domain"] for row in records}, {"minecraft"})

    def test_cli_invalid_limit(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "SSR", "--limit", "0"],
            capture_output=True, encoding="utf-8"
        )
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
