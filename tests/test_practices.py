import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from practices import (
    implementation_context, load_practices, read_object, validate_entry,
    validate_practices,
)
from search_concepts import load_abbreviations, load_concepts, load_guidance
from search_prompt import PromptIndex
from build_library import load_notes, render_library


class ImplementationGuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_concepts()
        cls.practices = load_practices()
        cls.index = PromptIndex(cls.records, load_guidance(), load_abbreviations(), cls.practices)

    def test_recipes_reference_existing_concepts_and_cover_domains(self):
        validate_practices(self.records, self.practices)
        self.assertTrue(self.practices["recipes"])
        for key, recipe in self.practices["recipes"].items():
            validate_entry(key, recipe)

    def test_majority_has_concept_specific_implementation_guides(self):
        self.assertGreater(len(self.practices["recipes"]), len(self.records) / 2)

    def test_specific_and_general_guidance_are_distinguished(self):
        record = next(row for row in self.records if row["id"] in self.practices["recipes"])
        specific = implementation_context(record, self.practices)
        self.assertEqual(specific["specificity"], "concept")
        self.assertEqual(specific["intent"], self.practices["recipes"][record["id"]]["intent"])
        general_data = copy.deepcopy(self.practices)
        general_data["recipes"].pop(record["id"])
        general = implementation_context(record, general_data)
        self.assertEqual(general["specificity"], "domain")
        self.assertIn("暂无专用", general["notice"])
        self.assertEqual(general["intent"], self.practices["domains"][record["domain"]]["intent"])

    def test_invalid_recipe_shapes_fail(self):
        valid = next(iter(self.practices["recipes"].values()))
        for field in ("intent", "principles", "implementation", "checks", "pitfalls"):
            entry = copy.deepcopy(valid)
            entry[field] = "" if field == "intent" else []
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_entry("XX001", entry)

    def test_unknown_id_and_incomplete_domains_fail(self):
        bad = copy.deepcopy(self.practices)
        bad["recipes"]["ZZ999"] = next(iter(bad["recipes"].values()))
        with self.assertRaises(ValueError):
            validate_practices(self.records, bad)
        bad = copy.deepcopy(self.practices)
        bad["domains"].pop(next(iter(bad["domains"])))
        with self.assertRaises(ValueError):
            validate_practices(self.records, bad)

    def test_duplicate_json_keys_fail(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"same":1,"same":2}', encoding="utf-8")
            with self.assertRaises(ValueError):
                read_object(path)

    def test_recipe_content_appears_on_reader_page(self):
        pages = render_library(self.records, load_notes(), load_abbreviations(), self.practices)
        for concept_id, recipe in self.practices["recipes"].items():
            with self.subTest(concept_id=concept_id):
                page = pages[f"concepts/{concept_id}.md"]
                self.assertIn(recipe["intent"], page)
                for field in ("principles", "implementation", "checks", "pitfalls"):
                    self.assertTrue(all(value in page for value in recipe[field]))

    def test_retrieval_returns_guidance_without_changing_candidate_status(self):
        concept_id = next(iter(self.practices["recipes"]))
        result = self.index.search(concept_id, limit=1)["results"][0]
        self.assertEqual(result["id"], concept_id)
        self.assertEqual(result["status"], "candidate")
        self.assertEqual(result["implementation_context"]["specificity"], "concept")

    def test_recipe_terms_can_retrieve_beyond_titles(self):
        records = [{
            "id": "XX001", "domain": "demo", "concept": "Opaque name",
            "cues": "Unrelated", "meaning": "Definition", "boundary": "Boundary",
            "path": "reference.md", "line": 1, "reader_link": "[demo](demo.md)",
        }]
        recipe = {
            "intent": "Useful mechanism",
            "principles": ["xylophone cobalt labyrinth zephyr quasar nebula"],
            "implementation": ["Apply the mechanism"],
            "checks": ["Inspect the outcome"], "pitfalls": ["No universal guarantee"],
        }
        practices = {
            "recipes": {"XX001": recipe}, "domains": {"demo": recipe},
            "sources": {"XX001": "references/demo-recipes.json"},
        }
        index = PromptIndex(records, {}, [], practices)
        result = index.search("xylophone cobalt labyrinth zephyr quasar nebula")["results"]
        self.assertEqual(result[0]["id"], "XX001")
        self.assertTrue(result[0]["match_evidence"]["implementation_terms"])

    def test_agent_cli_returns_implementation_context(self):
        result = subprocess.run(
            [sys.executable, "-B", str(ROOT / "scripts" / "search_concepts.py"),
             "NW012", "--agent", "--limit", "1"],
            capture_output=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = json.loads(result.stdout)
        self.assertEqual(rows[0]["id"], "NW012")
        self.assertIsNotNone(rows[0]["implementation_context"])


if __name__ == "__main__":
    unittest.main()
