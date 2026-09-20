from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_library
import search_concepts


class ReaderLibraryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = search_concepts.load_concepts()
        cls.notes = build_library.load_notes()
        cls.rendered = build_library.render_library(
            cls.records, cls.notes, search_concepts.load_abbreviations()
        )

    def test_all_domains_have_labels(self):
        self.assertEqual(set(build_library.LABELS), set(search_concepts.DOMAINS))

    def test_one_reader_page_per_concept(self):
        pages = {name for name in self.rendered if name.startswith("concepts/")}
        self.assertEqual(pages, {f'concepts/{row["id"]}.md' for row in self.records})

    def test_generated_content_is_current(self):
        self.assertEqual(build_library.check_library(self.rendered, ROOT / "library"), [])

    def test_search_links_target_actual_pages(self):
        for record in self.records:
            path = Path(record["reader_path"])
            self.assertTrue(path.is_file(), record["id"])
            text = path.read_text(encoding="utf-8")
            self.assertIn(record["concept"], text)
            self.assertIn(record["meaning"], text)
            self.assertIn(record["boundary"], text)
            self.assertIn(path.as_posix(), record["reader_link"])

    def test_pages_are_portable(self):
        for text in self.rendered.values():
            self.assertNotIn(ROOT.as_posix(), text)
            self.assertNotIn(str(ROOT), text)
            for target in re.findall(r"\]\(([^)]+)\)", text):
                self.assertFalse(Path(target).is_absolute())

    def test_relocated_search_uses_new_root(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "Installed Skill With Spaces"
            (destination / "references").mkdir(parents=True)
            for domain in search_concepts.DOMAINS:
                name = domain + ".md"
                shutil.copy2(ROOT / "references" / name, destination / "references" / name)
            records = search_concepts.load_concepts(destination)
            result = search_concepts.search(records, ["DP022"])[0]
            expected = destination / "library" / "concepts" / "DP022.md"
            self.assertEqual(Path(result["reader_path"]), expected)
            self.assertIn(f"<{expected.as_posix()}>", result["reader_link"])
            self.assertNotIn(ROOT.as_posix(), result["reader_link"])

    def test_invalid_notes_are_rejected(self):
        for invalid in (
            {"ZZ999": {"example": "Unknown", "related": []}},
            {"DP022": {"example": "", "related": []}},
            {"DP022": {"example": "Example", "related": ["ZZ999"]}},
        ):
            with self.subTest(notes=invalid), self.assertRaises(ValueError):
                build_library.validate_notes(self.records, invalid)

    def test_notes_and_related_links_are_rendered(self):
        for concept_id, note in self.notes.items():
            page = self.rendered[f"concepts/{concept_id}.md"]
            self.assertIn(note["example"], page)
            for related in note.get("related", []):
                self.assertIn(f"]({related}.md)", page)

    def test_check_detects_missing_stale_and_extra(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            self.assertTrue(build_library.check_library({"index.md": "expected"}, directory))
            (directory / "index.md").write_text("old", encoding="utf-8")
            (directory / "extra.md").write_text("extra", encoding="utf-8")
            problems = build_library.check_library({"index.md": "expected"}, directory)
            self.assertEqual(len(problems), 2)

    def test_source_ids_have_entries(self):
        source_text = (ROOT / "references" / "sources.md").read_text(encoding="utf-8")
        available = set(re.findall(r"^\| (S\d{2}) \|", source_text, re.MULTILINE))
        for domain in search_concepts.DOMAINS:
            text = (ROOT / "references" / (domain + ".md")).read_text(encoding="utf-8")
            for source_id in re.findall(r"\bS\d{2}\b", text):
                self.assertIn(source_id, available, (domain, source_id))


if __name__ == "__main__":
    unittest.main()
