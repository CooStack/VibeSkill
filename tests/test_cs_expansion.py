import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from search_concepts import (
    abbreviation_matches, load_abbreviations, load_concepts, load_guidance, search,
)
from search_prompt import PromptIndex


class ComputerScienceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = load_concepts()
        cls.abbreviations = load_abbreviations()
        cls.index = PromptIndex(cls.records, load_guidance(), cls.abbreviations)

    def test_specialist_concept_lookup(self):
        cases = [
            ("字节顺序", "hw", "HW003"),
            ("写时复制", "os", "OS009"),
            ("CIDR", "network", "NW006"),
            ("动态规划", "algo", "AL005"),
            ("AST", "compiler", "LC003"),
            ("AEAD", "sec", "SE010"),
            ("CRDT", "dist", "DC018"),
            ("Watermark", "data", "DE010"),
            ("RAG", "ml", "ML021"),
            ("RTO", "sre", "RE017"),
            ("停机问题", "theory", "TC008"),
            ("WCET", "iot", "EM005"),
            ("差分隐私", "hci", "HC008"),
        ]
        for term, domain, concept_id in cases:
            with self.subTest(term=term):
                result = search(
                    self.records, [term], domain=domain, limit=3,
                    abbreviations=self.abbreviations,
                )
                self.assertIn(concept_id, {row["id"] for row in result})

    def test_full_prompts_find_cross_layer_problems(self):
        cases = [
            ("TCP 收到半条消息，不要改现有协议", "NW012"),
            ("容器 OOM 后进程被杀，先查内存限制", "OS028"),
            ("DNS 已修改却还访问旧地址", "NW023"),
            ("模型离线准确率很高上线很差，只分析数据泄漏", "ML006"),
            ("任务依赖需要拓扑排序并检测环", "AL016"),
            ("锁过期后旧任务仍写数据，考虑 fencing token", "DC014"),
            ("乱序数据的 watermark 怎么定义", "DE010"),
            ("连续攻击音效重复很机械，不要只加响度", "AU013"),
            ("半透明粒子与地面交界不要有硬边，不要改碰撞", "CG040"),
            ("苹果的玻璃风格用于网页，保留可读性", "DL002"),
            ("帮我优化提示词：做个连续挥剑砍击音效，听起来有重量，不要靠更大声，不换现有引擎", "AU031"),
        ]
        for prompt, concept_id in cases:
            with self.subTest(prompt=prompt):
                result = self.index.search(prompt, limit=3)
                self.assertIn(concept_id, {row["id"] for row in result["results"]})

    def test_new_abbreviation_ambiguities_are_retained(self):
        expected = {
            "DP": {"AL005", "DP001", "HC008"},
            "CS": {"GL016", "TC001"},
            "MAC": {"SE011", "NW004"},
            "CFG": {"LC012", "TC004"},
            "ANN": {"DE017", "ML016"},
            "SMT": {"HW008", "TC012"},
            "FP": {"LC022", "HW004", "ML010"},
        }
        for alias, ids in expected.items():
            with self.subTest(alias=alias):
                matched = abbreviation_matches(alias, self.abbreviations)
                actual = {
                    concept_id for entry in matched
                    for meaning in entry["meanings"] for concept_id in meaning["ids"]
                }
                self.assertTrue(ids <= actual)

    def test_domain_filter_keeps_raw_ambiguity(self):
        result = self.index.search("DP", domain="algo", limit=10)
        self.assertTrue(all(row["domain"] == "algorithms" for row in result["results"]))
        entry = next(item for item in result["abbreviation_candidates"] if item["alias"] == "DP")
        self.assertEqual(len(entry["meanings"]), 3)

    def test_constraints_survive_rich_retrieval(self):
        result = self.index.search("TCP 收到半条消息，不要改现有协议", limit=1)
        self.assertIn("不要改现有协议", result["constraints_verbatim"])
        self.assertEqual(result["results"][0]["id"], "NW012")
        self.assertEqual(result["results"][0]["status"], "candidate")

    def test_platform_constraint_is_preserved(self):
        result = self.index.search("优化提示词：给现有Vue后台加苹果玻璃风格，不改页面布局，要在普通Windows浏览器也可用")
        self.assertIn("要在普通Windows浏览器也可用", result["constraints_verbatim"])
        self.assertIn("不改页面布局", result["constraints_verbatim"])


if __name__ == "__main__":
    unittest.main()
