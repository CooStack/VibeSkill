"""Retrieve concept context from a full prompt, offline and without executing it."""

import argparse
from collections import Counter, defaultdict
import json
import math
from pathlib import Path
import re
import sys
import time

from search_concepts import (
    DOMAINS, DOMAIN_ALIASES, abbreviation_matches, agent_record, contains,
    load_abbreviations, load_concepts, load_search_records, load_guidance, normalize, positive_int,
    validate_metadata,
)
from practices import implementation_context, load_practices, validate_practices


MAX_PROMPT_CHARS = 20000
STOPWORDS = set(
    "a an the and or to of in on is it for with use using please help "
    "this that me my make do code function feature implement improve "
    "帮我 请帮 请你 一下 一个 这个 那个 实现 功能 优化 问题 需要 "
    "可以 相关 进行 使用 处理 支持 对应 现有 不要 不许 提示 示词 提示词".split()
)
DOMAIN_HINTS = {
    "vue": "vue", "mysql": "mysql", "spring": "spring", "kotlin": "kotlin",
    "java": "java", "typescript": "typescript", "javascript": "javascript",
    "opengl": "opengl", "minecraft": "minecraft", "vert.x": "vertx",
    "vertx": "vertx", "css": "css", "html": "html",
    "音效": "audio", "游戏音频": "audio",
}


def tokens(text):
    text = normalize(text)
    result = set(re.findall(r"[a-z][a-z0-9_]*(?:[.-][a-z0-9_]+)*", text))
    for run in re.findall(r"[\u3400-\u9fff]+", text):
        for width in (2, 3):
            result.update(run[index:index + width] for index in range(len(run) - width + 1))
    return result - STOPWORDS


def phrase_parts(text):
    return {
        normalize(part.strip()) for part in re.split(r"[;；、，,/]", text)
        if 2 <= len(part.strip()) <= 60 and normalize(part.strip()) not in STOPWORDS
    }


def prompt_context(text):
    # These are literal hints, not a semantic intent or permission classifier.
    head = re.split(r"[:：\n“\"「]", text, maxsplit=1)[0]
    rewrite = (
        re.search(r"(优化|改写|润色|整理|补全|完善|改进).{0,24}(提示词|prompt)", head, re.I)
        or re.search(r"(提示词|prompt).{0,12}(优化|改写|润色)", head, re.I)
        or re.search(r"\b(rewrite|refine)\b.{0,40}\bprompt\b", head, re.I)
    )
    execute = re.search(r"(实现|修复|开发|重构|修改|排查|优化).{0,12}", head)
    question = re.search(
        r"^(?:(?:请帮我|帮我|请)\s*)?"
        r"(?:解释|讲解|说明|什么是|什么叫|为什么|为何|如何|怎样|怎么|我想知道|我想了解|"
        r"what\b|why\b|how\b)", head, re.I,
    ) or re.search(r"(?<!不要)(?<!不是)(?<!别)(?:只|先)(?:解释|回答|讨论)", head)
    mixed = question and re.search(r"(?:并|然后|再|同时)(?:请|帮我)?(?:实现|修复|修改|开发|执行)", head)
    clauses = [part.strip() for part in re.split(r"[，,。！？!?\n；;]", text) if part.strip()]
    constraint_pattern = re.compile(
        r"不要|不许|禁止|不得|别(?:改|加|动|换|删|用)|不(?:加|改|删|换|使用|引入|联网)|"
        r"只(?:分析|解释|改写|修改|改|给|用|允许|输出)|保持|保留|沿用|不能|必须|"
        r"(?:需要|要)(?:在|用|支持|兼容)|"
        r"\b(?:do not|don't|must|only|without|keep|preserve|no new)\b", re.I
    )
    return {
        "mode_hint": (
            "rewrite" if rewrite else "mixed" if mixed else "question" if question
            else "implementation_or_analysis" if execute else "unspecified"
        ),
        "constraints_verbatim": [part for part in clauses if constraint_pattern.search(part)],
        "notice": "模式与限制仅为词面提示；原文才是依据。候选/匹配分数不代表确定意图、采用概率或执行授权。",
        "mapping_notice": "先比较目标和语义再采用候选；用户自定义概念及无匹配片段保留原意，不强制替换。纯提问只回答，不因出现实施术语就执行。",
    }


class PromptIndex:
    def __init__(self, records, guidance, abbreviations, practices=None):
        validate_metadata(records, guidance, abbreviations)
        self.practices = load_practices() if practices is None else practices
        validate_practices(records, self.practices)
        self.records = records
        self.guidance = guidance
        self.abbreviations = abbreviations
        self.postings = defaultdict(dict)
        self.recipe_postings = defaultdict(set)
        self.phrases = {}
        self.lengths = {}
        for index, record in enumerate(records):
            weights = Counter()
            for field, weight in (("concept", 3.0), ("cues", 3.0), ("meaning", 1.0), ("boundary", 0.5)):
                for token in tokens(record[field]):
                    weights[token] += weight
            self.lengths[index] = max(len(weights), 1)
            for token, weight in weights.items():
                self.postings[token][index] = weight
            self.phrases[index] = phrase_parts(record["concept"]) | phrase_parts(record["cues"])
            if record.get("personal"):
                # User-defined names may legitimately be one Han character.
                self.phrases[index].update(
                    normalize(alias.strip()) for alias in record["concept"].split(";")
                    if len(alias.strip()) == 1
                )
            recipe = record.get("implementation_recipe") or self.practices["recipes"].get(record["id"])
            if recipe:
                recipe_text = " ".join(
                    [recipe["intent"]] + recipe["principles"] + recipe["implementation"]
                )
                for token in tokens(recipe_text):
                    self.recipe_postings[token].add(index)
        count = len(records)
        self.idf = {
            term: math.log(1.0 + (count + 1) / (len(posting) + 1))
            for term, posting in self.postings.items()
        }

    def search(self, prompt, limit=8, domain=None):
        if not prompt.strip():
            raise ValueError("Prompt must not be empty")
        if len(prompt) > MAX_PROMPT_CHARS:
            raise ValueError(f"Prompt exceeds {MAX_PROMPT_CHARS} characters; narrow the task context")
        domain = DOMAIN_ALIASES.get(domain, domain)
        if domain and domain not in DOMAINS and domain != "user":
            raise ValueError(f"Unknown domain: {domain}")
        query_tokens = tokens(prompt)
        score = defaultdict(float)
        evidence = defaultdict(set)
        recipe_evidence = defaultdict(set)
        for term in query_tokens:
            for index, weight in self.postings.get(term, {}).items():
                score[index] += self.idf[term] * math.log1p(weight) / math.sqrt(self.lengths[index])
                evidence[index].add(term)
            for index in self.recipe_postings.get(term, ()):
                recipe_evidence[index].add(term)
        expansions = abbreviation_matches(prompt, self.abbreviations)
        alias_ids = defaultdict(list)
        for entry in expansions:
            for meaning in entry["meanings"]:
                for concept_id in meaning["ids"]:
                    alias_ids[concept_id].append({"alias": entry["alias"], "expansion": meaning["expansion"]})
        hinted_domains = {
            name for term, name in DOMAIN_HINTS.items() if contains(prompt, normalize(term))
        }
        results = []
        for index, record in enumerate(self.records):
            if domain == "user" and not record.get("personal"):
                continue
            if domain and domain != "user" and record["domain"] != domain:
                continue
            concept_id = record["id"]
            phrases = sorted(phrase for phrase in self.phrases[index] if contains(prompt, phrase))
            rules = self.guidance.get(concept_id, {}).get("signals", [])
            signals = [rule for rule in rules if all(contains(prompt, normalize(part)) for part in rule)]
            aliases = alias_ids.get(concept_id, [])
            direct_id = contains(prompt, normalize(concept_id))
            value = score[index]
            recipe_terms = recipe_evidence[index]
            novel_recipe_terms = recipe_terms - evidence[index]
            if len(novel_recipe_terms) >= 3:
                # Recipes supplement retrieval; broad implementation prose must not
                # outweigh an explicit term, abbreviation, ID, or requirement signal.
                value += min(len(novel_recipe_terms) * 0.35, 3.0)
            if not (phrases or signals or aliases or direct_id) and (
                (len(evidence[index]) < 2 and len(recipe_terms) < 3) or value < 1.5
            ):
                continue
            value += min(len(phrases), 3) * 5 + (24 if signals else 0) + (18 if aliases else 0)
            value += 60 if direct_id else 0
            value += 2 if record["domain"] in hinted_domains else 0
            if value <= 0:
                continue
            results.append(agent_record(record, self.guidance) | {
                "retrieval_score": round(value, 4),
                "match_evidence": {
                    "phrases": phrases[:8],
                    "signals": signals,
                    "abbreviations": aliases,
                    "terms": sorted(evidence[index], key=lambda term: (-self.idf.get(term, 0), term))[:8],
                    "exact_id": direct_id,
                    "implementation_terms": sorted(recipe_terms)[:8],
                },
                "reader_link": record["reader_link"],
            })
        results.sort(key=lambda row: (-row["retrieval_score"], row["id"]))
        if results:
            floor = results[0]["retrieval_score"] * 0.35
            results = [
                row for row in results
                if row["retrieval_score"] >= floor
                or row["match_evidence"]["signals"]
                or row["match_evidence"]["abbreviations"]
                or row["match_evidence"]["exact_id"]
            ]
        selected = results[:limit]
        by_id = {record["id"]: record for record in self.records}
        for row in selected:
            row["implementation_context"] = implementation_context(by_id[row["id"]], self.practices)
        return prompt_context(prompt) | {
            "abbreviation_candidates": expansions,
            "results": selected,
            "fallback": None if results else "没有可靠词面命中；由智能体提取具体对象/症状或换同义词，不强行推荐概念。",
        }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", nargs="?", help="A quoted full prompt.")
    inputs = parser.add_mutually_exclusive_group()
    inputs.add_argument("--stdin", action="store_true", help="Read UTF-8 text from stdin.")
    inputs.add_argument("--file", type=Path, help="Read a UTF-8 prompt file, without executing its contents.")
    parser.add_argument("--limit", type=positive_int, default=8)
    parser.add_argument("--domain", choices=sorted(set(DOMAINS) | set(DOMAIN_ALIASES) | {"user"}))
    parser.add_argument("--project", type=Path, help="Project scope for personal knowledge; defaults to the current directory.")
    parser.add_argument("--builtin-only", action="store_true", help="Exclude personal knowledge.")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args(argv)
    if sum((args.prompt is not None, args.stdin, args.file is not None)) != 1:
        parser.error("provide exactly one of prompt, --stdin, or --file")
    started = time.perf_counter()
    try:
        if args.file is not None:
            with args.file.open(encoding="utf-8-sig") as handle:
                prompt = handle.read(MAX_PROMPT_CHARS + 1)
        elif args.stdin:
            prompt = sys.stdin.read(MAX_PROMPT_CHARS + 1)
        else:
            prompt = args.prompt
        index = PromptIndex(
            load_search_records(project=args.project, include_user=not args.builtin_only),
            load_guidance(), load_abbreviations(),
        )
        response = index.search(prompt, args.limit, args.domain)
        response["elapsed_ms"] = round((time.perf_counter() - started) * 1000, 2)
        if args.format == "json":
            print(json.dumps(response, ensure_ascii=False, indent=2))
        else:
            print(response["notice"])
            for constraint in response["constraints_verbatim"]:
                print(f"\nConstraint: {constraint}")
            for row in response["results"]:
                print(f'\n- {row["reader_link"]}: {row["meaning"]}')
                print(f'  Boundary: {row["boundary"]}')
                if row["guidance"]:
                    print(f'  Requirement: {row["guidance"]["translate_to"]}')
                context = row["implementation_context"]
                print(f'  Implementation ({context["specificity"]}): {context["intent"]}')
                for step in context["implementation"]:
                    print(f"  - {step}")
                print("  Checks: " + "；".join(context["checks"]))
                print("  Scope: " + context["notice"])
            if response["fallback"]:
                print(response["fallback"])
        return 0 if response["results"] else 1
    except (OSError, ValueError) as error:
        print(f"Cannot search prompt: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    raise SystemExit(main())
