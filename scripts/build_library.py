"""Generate portable reader pages from concept tables and curated reader notes."""

import argparse
import json
from pathlib import Path
import sys

from search_concepts import DOMAINS, ROOT, load_abbreviations, load_concepts, validate_metadata
from practices import load_practices, recipe_markdown, validate_practices


LABELS = {
    "backend": "后端", "web": "网页与 Web 平台", "frontend": "前端工程",
    "game": "游戏开发", "design": "设计", "art": "美术", "modeling": "三维建模",
    "java": "Java 与 JVM", "kotlin": "Kotlin", "html": "HTML", "css": "CSS",
    "javascript": "JavaScript", "typescript": "TypeScript", "vue": "Vue",
    "minecraft": "Minecraft / 我的世界", "tooling": "构建与工具链",
    "mysql": "MySQL", "spring": "Spring", "vertx": "Vert.x 与 Vertex 消歧",
    "data-structures": "数据结构", "design-patterns": "设计模式",
    "opengl": "OpenGL 与 GPU 接口", "graphics": "计算机图形学与特效",
    "mathematics": "数学与计算应用",
    "prompting": "编程提示词与任务规格",
    "engineering": "工程表达与常见简写",
    "architecture": "计算机体系结构与数字表示",
    "operating-systems": "操作系统与系统编程",
    "networking": "计算机网络与互联网",
    "algorithms": "算法设计与分析",
    "languages-compilers": "程序语言与编译系统",
    "security": "安全与密码学",
    "distributed": "分布式系统",
    "data-engineering": "数据工程、存储与检索",
    "machine-learning": "人工智能与机器学习",
    "reliability": "可靠性、云基础设施与质量验证",
    "computation-theory": "计算理论、逻辑与信息",
    "embedded": "嵌入式、实时系统与物联网",
    "human-computing": "人与计算、隐私及专业责任",
    "audio": "音效设计与游戏音频",
    "design-language": "设计语言与风格实现",
}
EXTRA_GUIDES = {
    "audio": ("audio-design-guide.md", "音效设计完整流程"),
    "design-language": ("design-language-guide.md", "玻璃材料 HTML/CSS 示例"),
}


def load_notes(root=ROOT):
    return json.loads((root / "references" / "reader-notes.json").read_text(encoding="utf-8"))


def validate_notes(records, notes):
    ids = {row["id"] for row in records}
    for concept_id, note in notes.items():
        if concept_id not in ids:
            raise ValueError(f"Unknown reader note ID: {concept_id}")
        if not isinstance(note, dict) or not isinstance(note.get("example"), str) or not note["example"].strip():
            raise ValueError(f"{concept_id}: expected a nonempty example")
        related = note.get("related", [])
        if not isinstance(related, list) or any(item not in ids for item in related):
            raise ValueError(f"{concept_id}: invalid related IDs")


def render_library(records, notes, abbreviations=None, practices=None):
    validate_notes(records, notes)
    practices = load_practices() if practices is None else practices
    validate_practices(records, practices)
    by_id = {row["id"]: row for row in records}
    files = {}
    index = [
        "# 用户概念库", "",
        "从需求中的说法找到专业名称，点开名称查看含义、适用情境和容易混淆的边界。",
        "本库主要支撑智能体的编程提示词优化；这里是可选阅读层，日常不需要逐项阅读。",
        "每个稳定 ID 对应一个概念或紧密相关的概念组；组内术语不一定完全同义。",
        f"当前收录 **{len(records)} 组概念**，按 **{len(DOMAINS)} 个领域/技术栈**组织。", "",
        f'其中 **{len(practices["recipes"])} 组**有概念专用实施指南；其余提供定义、边界及领域方法，不冒充完整教程。',
        "实施指南覆盖关键特征、落实步骤、验收与误用；不能把候选方案当成用户新增要求。", "",
        "## 按领域查看", "",
        "| 领域 | 条目数 |", "| --- | --- |",
    ]
    for domain in DOMAINS:
        rows = [row for row in records if row["domain"] == domain]
        label = LABELS[domain]
        index.append(f"| [{label}](domains/{domain}.md) | {len(rows)} |")
        domain_lines = [
            f"# {label}", "",
            "[返回总目录](../index.md)", "",
            "选择概念名称查看说明。需求线索是候选提示，不代表必须采用该方案。", "",
            "| 概念 | 你可能遇到的问题 |", "| --- | --- |",
        ]
        for row in rows:
            concept_id = row["id"]
            domain_lines.append(
                f'| [{concept_id} · {row["concept"]}](../concepts/{concept_id}.md) | {row["cues"]} |'
            )
            note = notes.get(concept_id, {})
            page = [
                f'# {row["concept"]}', "",
                f'**索引：{concept_id} · {label}**', "",
                f'[领域目录](../domains/{domain}.md) · [概念库总目录](../index.md)', "",
                "## 这是什么", "", row["meaning"], "",
                "## 什么时候会想到它", "",
                f'当你描述“{row["cues"]}”这类需求时，可以把本条作为候选概念。',
                "是否采用仍取决于实际目标、现有实现及约束。", "",
                "## 容易混淆的地方", "", row["boundary"], "",
            ]
            if note:
                page.extend(["## 例子", "", note["example"], ""])
            recipe = practices["recipes"].get(concept_id)
            if recipe:
                page.extend(["## 实施指南", "", "这是候选实施方法，需结合任务范围与项目环境采用。", ""])
                page.extend(recipe_markdown(recipe))
            else:
                page.extend([
                    "## 实施深度", "",
                    "本条暂无专用实施配方。上面的定义与边界用于消歧；",
                    f'[领域方法](../domains/{domain}.md)提供落实与验收基线，但不能代替具体机制的资料核对。', "",
                ])
            related = note.get("related", [])
            if related:
                page.extend(["## 关联概念", ""])
                for other_id in related:
                    page.append(f'- [{by_id[other_id]["concept"]}]({other_id}.md)')
                page.append("")
            page.extend([
                "## 进一步核对", "",
                f'[所属领域参考与资料入口](../../references/{domain}.md)',
                " · [来源核查范围](../../references/sources.md)", "",
                "这是概念摘要，不是完整教程或逐条验证的 API 契约。"
                "涉及版本、框架、公式或 GPU 行为时，应核对项目环境、定义及对应官方资料。", "",
            ])
            if domain in EXTRA_GUIDES:
                guide, guide_label = EXTRA_GUIDES[domain]
                page.extend([f"[{guide_label}](../../references/{guide})", ""])
            files[f"concepts/{concept_id}.md"] = "\n".join(page)
        domain_lines.extend(["", "## 领域实施方法", "", "以下为领域基线，不是每个概念的专用配方。", ""])
        domain_lines.extend(recipe_markdown(practices["domains"][domain]))
        files[f"domains/{domain}.md"] = "\n".join(domain_lines).rstrip() + "\n"
    index.extend([
        "", "## 从问题查找", "",
        "[需求路由与同名消歧](../references/routing.md)提供跨领域的口语需求映射。",
        "例如 Vertex 可能指图形顶点、图论顶点、Vert.x 或云平台名称；需要结合上下文辨别。",
        "", "## 阅读说明", "",
        "同一领域的摘要与阅读页来自同一份资料，维护时自动生成以避免内容分叉。"
        "概念库可持续补充，不声称穷尽所有知识。", "",
        "[来源与核查范围](../references/sources.md) · [Skill 使用规则](../SKILL.md)", "",
    ])
    files["index.md"] = "\n".join(index)
    coverage = [
        "# 实施深度覆盖", "", "[返回概念库](index.md)", "",
        "分别统计专用实施指南与基础概念层。基础层仍有定义、需求线索、边界及领域方法，",
        "但不据此声称已有每个概念的专用教程。部分原子概念定义已足够；复杂概念按真实需求继续深化。",
        "统计只证明资料存在，不证明实现、审美效果或全部事实已通过验证。", "",
        "| 领域 | 概念组 | 专用实施指南 | 基础概念层 |",
        "| --- | --- | --- | --- |",
    ]
    for domain in DOMAINS:
        rows = [row for row in records if row["domain"] == domain]
        specific = sum(row["id"] in practices["recipes"] for row in rows)
        coverage.append(
            f"| [{LABELS[domain]}](domains/{domain}.md) | {len(rows)} | {specific} | {len(rows) - specific} |"
        )
    coverage.extend(["", "## 基础层条目", "", "以下列表用于维护选题，不表示每一条都必须扩成教程。", ""])
    for domain in DOMAINS:
        basic = [
            f'[{row["id"]}](concepts/{row["id"]}.md)' for row in records
            if row["domain"] == domain and row["id"] not in practices["recipes"]
        ]
        if basic:
            coverage.extend([f"### {LABELS[domain]}", "", "、".join(basic), ""])
    files["coverage.md"] = "\n".join(coverage)
    files["index.md"] += "\n[实施深度覆盖统计](coverage.md)\n"
    if abbreviations is not None:
        validate_metadata(records, {}, abbreviations)
        lines = [
            "# 简写与别名索引", "", "[返回概念库](index.md)", "",
            "缩写可能跨领域重名；以下是候选含义，不是自动纠正。", "",
            "| 简写/别名 | 展开及语境 | 概念 |", "| --- | --- | --- |",
        ]
        for entry in abbreviations:
            for meaning in entry["meanings"]:
                links = "、".join(
                    f'[{concept_id}](concepts/{concept_id}.md)' for concept_id in meaning["ids"]
                )
                lines.append(f'| {entry["alias"]} | {meaning["expansion"]} | {links} |')
        files["abbreviations.md"] = "\n".join(lines) + "\n"
        files["index.md"] += "\n[简写与别名索引](abbreviations.md)\n"
    return files


def check_library(files, directory):
    problems = []
    for relative, content in files.items():
        path = directory / relative
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            problems.append(f"Missing or stale: {path}")
    if directory.exists():
        expected = set(files)
        for path in directory.rglob("*.md"):
            if path.relative_to(directory).as_posix() not in expected:
                problems.append(f"Unexpected generated page: {path}")
    return problems


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify without writing.")
    args = parser.parse_args(argv)
    try:
        files = render_library(load_concepts(), load_notes(), load_abbreviations())
        directory = ROOT / "library"
        if args.check:
            problems = check_library(files, directory)
            if problems:
                print("\n".join(problems), file=sys.stderr)
                return 1
            print(f"Reader library is current: {len(files)} pages.")
        else:
            for relative, content in files.items():
                path = directory / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8", newline="\n")
            print(f"Generated {len(files)} reader pages in {directory}.")
        return 0
    except (OSError, ValueError) as error:
        print(f"Cannot build reader library: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
