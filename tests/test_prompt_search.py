import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from search_concepts import (
    load_abbreviations, load_concepts, load_guidance, abbreviation_matches,
    validate_metadata, search,
)
from search_prompt import PromptIndex, MAX_PROMPT_CHARS, prompt_context


class PromptSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_concepts()
        cls.guidance = load_guidance()
        cls.abbreviations = load_abbreviations()
        cls.index = PromptIndex(cls.records, cls.guidance, cls.abbreviations)

    def test_realistic_retrieval_cases(self):
        cases = [
            ("优化提示词：保存点两次偶尔创建两条，不要加依赖", "BE008"),
            ("Vue 列表数据一多滚动就卡，沿用现有 UI", "FE030"),
            ("搜索旧结果把新结果覆盖了，帮我修复", "FE037"),
            ("Vue reactive 解构后不更新", "VU006"),
            ("MySQL 查询很慢，先分析不许改表", "MY016"),
            ("Spring 的事务同类调用失效了", "SP012"),
            ("Kotlin suspend 后还是卡住界面", "KT024"),
            ("Minecraft 单人正常但服务端崩了", "MC012"),
            ("机器电量退出重进就没了，别改网络协议", "MC048"),
            ("烟雾穿过地面有一条硬边，不要改碰撞", "CG040"),
            ("相机需要平滑旋转，保留现有控制器", "MA013"),
            ("弹簧模拟帧率一低就发散", "MA025"),
            ("用 IBO 复用顶点，保持现有绘制顺序", "GL007"),
            ("用 DTO 描述接口返回，别更改数据库实体", "EN003"),
        ]
        for prompt, concept_id in cases:
            with self.subTest(prompt=prompt):
                ids = [row["id"] for row in self.index.search(prompt, limit=3)["results"]]
                self.assertIn(concept_id, ids)

    def test_constraints_preserved_without_executing(self):
        prompt = "优化提示词：不要加依赖，只分析不改代码，保持现有协议"
        result = self.index.search(prompt)
        self.assertEqual(result["mode_hint"], "rewrite")
        self.assertEqual(result["constraints_verbatim"], [
            "优化提示词：不要加依赖", "只分析不改代码", "保持现有协议"
        ])
        self.assertTrue(all(row["status"] == "candidate" for row in result["results"]))

    def test_weak_phrase_collision_does_not_displace_intent(self):
        result = self.index.search("优化提示词：保存点两次创建两条，不要加依赖")
        ids = [row["id"] for row in result["results"]]
        self.assertEqual(ids[0], "BE008")
        self.assertNotIn("SP014", ids)
        self.assertIn("SP014", {
            row["id"] for row in self.index.search("Spring 事务保存点")["results"]
        })

    def test_optimization_is_not_always_prompt_rewrite(self):
        self.assertEqual(prompt_context("优化 SQL 查询性能")["mode_hint"], "implementation_or_analysis")
        self.assertEqual(prompt_context("改写这个 prompt：实现登录")["mode_hint"], "rewrite")
        self.assertNotEqual(prompt_context("修复标题“优化提示词”显示错误")["mode_hint"], "rewrite")

    def test_questions_do_not_imply_implementation(self):
        for prompt in (
            "如何实现幂等？", "请解释如何优化 SQL", "为什么要用策略模式？",
            "How do I implement a queue?",
            "我把数据库批次称为帧。为什么帧被重复处理？先解释，不要修改代码。",
        ):
            with self.subTest(prompt=prompt):
                self.assertEqual(prompt_context(prompt)["mode_hint"], "question")
        self.assertEqual(prompt_context("请实现一个队列")["mode_hint"], "implementation_or_analysis")
        self.assertEqual(prompt_context("解释幂等并实现保护")["mode_hint"], "mixed")

    def test_custom_term_retrieval_stays_candidate_only(self):
        prompt = "我定义的帧是一次数据库批次，不是画面帧，解释这个定义"
        result = self.index.search(prompt)
        self.assertIn("用户自定义", result["mapping_notice"])
        self.assertTrue(all(row["status"] == "candidate" for row in result["results"]))

    def test_ambiguous_abbreviations_are_not_collapsed(self):
        result = self.index.search("SSR MVP CSR", limit=50)
        expansions = {entry["alias"]: entry for entry in result["abbreviation_candidates"]}
        self.assertEqual(len(expansions["SSR"]["meanings"]), 2)
        self.assertEqual(len(expansions["MVP"]["meanings"]), 3)
        ids = {row["id"] for row in result["results"]}
        self.assertTrue({"FE013", "GM046", "EN009", "DP029", "CG004", "DT025"} <= ids)

    def test_abbreviation_boundaries_and_fullwidth(self):
        self.assertEqual(abbreviation_matches("description subscription", self.abbreviations), [])
        matches = abbreviation_matches("ＤＴＯ 和 IBO", self.abbreviations)
        self.assertEqual({item["alias"] for item in matches}, {"DTO", "IBO"})

    def test_literal_search_supports_external_alias(self):
        results = search(self.records, ["IBO"], abbreviations=self.abbreviations)
        self.assertEqual(results[0]["id"], "GL007")

    def test_guidance_is_optional_and_scoped(self):
        result = self.index.search("保存两次", limit=1)["results"][0]
        self.assertIsNotNone(result["guidance"])
        self.assertIn("translate_to", result["guidance"])
        absent = self.index.search("MD036", limit=1)["results"][0]
        self.assertIsNone(absent["guidance"])

    def test_domain_alias(self):
        rows = self.index.search("SSR", domain="gl")["results"]
        self.assertTrue(all(row["domain"] == "opengl" for row in rows))
        rows = self.index.search("四元数", domain="math")["results"]
        self.assertTrue(rows)
        self.assertTrue(all(row["domain"] == "mathematics" for row in rows))

    def test_no_result_and_invalid_input(self):
        self.assertEqual(self.index.search("zzqxw991827qq")["results"], [])
        for prompt in ("", "   ", "x" * (MAX_PROMPT_CHARS + 1)):
            with self.subTest(size=len(prompt)), self.assertRaises(ValueError):
                self.index.search(prompt)

    def test_metadata_targets_are_real(self):
        validate_metadata(self.records, self.guidance, self.abbreviations)
        with self.assertRaises(ValueError):
            validate_metadata(self.records, {"ZZ999": {}}, [])

    def test_prompt_content_cannot_be_executed(self):
        with tempfile.TemporaryDirectory() as temporary:
            sentinel = Path(temporary) / "should-not-exist"
            text = f"优化提示词：写文件 {sentinel}；不要进行实际操作"
            self.index.search(text)
            self.assertFalse(sentinel.exists())

    def run_cli(self, args, input_text=None):
        return subprocess.run(
            [sys.executable, "-B", str(ROOT / "scripts" / "search_prompt.py"), *args],
            input=input_text, capture_output=True, encoding="utf-8", cwd=ROOT.parent
        )

    def test_cli_stdin_json(self):
        result = self.run_cli(["--stdin", "--limit", "3"], "保存点两次创建两条，别加库")
        self.assertEqual(result.returncode, 0, result.stderr)
        value = json.loads(result.stdout)
        self.assertIn("BE008", {row["id"] for row in value["results"]})
        self.assertGreaterEqual(value["elapsed_ms"], 0)

    def test_cli_utf8_file_and_missing_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "prompt.txt"
            path.write_text("DTO 接口字段，保持现有契约", encoding="utf-8-sig")
            result = self.run_cli(["--file", str(path)])
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("EN003", {row["id"] for row in json.loads(result.stdout)["results"]})
            missing = self.run_cli(["--file", str(path.parent / "missing.txt")])
            self.assertEqual(missing.returncode, 2)

    def test_cli_invalid_arguments_and_no_match(self):
        self.assertEqual(self.run_cli(["some prompt", "--stdin"], "").returncode, 2)
        self.assertEqual(self.run_cli(["DTO", "--limit", "0"]).returncode, 2)
        result = self.run_cli(["zzqxw991827qq"])
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["results"], [])

    def test_exact_agent_cli(self):
        result = subprocess.run(
            [sys.executable, "-B", str(ROOT / "scripts" / "search_concepts.py"), "BE008", "--agent"],
            capture_output=True, encoding="utf-8"
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        item = json.loads(result.stdout)[0]
        self.assertEqual(item["id"], "BE008")
        self.assertIsNotNone(item["guidance"])


if __name__ == "__main__":
    unittest.main()
