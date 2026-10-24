"""Score the knowledge service against the 50-question golden set.

    python -m eval.knowledge_eval
    python -m eval.knowledge_eval --limit 10        # quick pass while iterating
    python -m eval.knowledge_eval --retrieval-only  # no model calls, no cost

Metrics:

  retrieval hit rate     the expected document appears anywhere in the chunks
                         kept after reranking. This is the ceiling on quality:
                         the generator cannot be right about a document it
                         never saw.
  retrieval hit rate @1  the top chunk after reranking is from the expected
                         document. Harsher, and the number that moves when you
                         change the reranker.
  faithfulness           every claim in the answer is supported by the
                         retrieved context, judged by a model.
  correctness            the answer conveys the reference answer.
  abstention             how often the system said NOT_COVERED. Every golden
                         question is answerable, so each one is a miss.

Results are written to eval_results/knowledge_eval.json so two runs can be
compared directly.
"""

from __future__ import annotations

import argparse
import json
import time
from collections import defaultdict
from pathlib import Path

from eval.judges import judge_correctness, judge_faithfulness, judges_available
from knowledge.answer import NOT_COVERED, answer_question, build_context
from knowledge.retrieval import search
from shared.config import DATA_DIR, EVAL_DIR, settings
from shared.usage import track


def load_golden_set(limit: int | None = None) -> list[dict]:
    path = DATA_DIR / "golden_set.json"
    if not path.exists():
        raise RuntimeError("No golden_set.json. Run `python -m data.generate` first.")
    items = json.loads(path.read_text(encoding="utf-8"))
    return items[:limit] if limit else items


def expected_source(item: dict) -> str:
    return f"{item['expected_doc']}.md"


def evaluate(items: list[dict], retrieval_only: bool = False) -> dict:
    judged = judges_available() and not retrieval_only
    records: list[dict] = []
    started = time.time()

    for position, item in enumerate(items, start=1):
        wanted = expected_source(item)

        # The system's own cost and time, measured apart from the judges, so
        # the per-question figures describe what a real user request costs.
        asked_at = time.perf_counter()
        with track() as system_usage:
            if retrieval_only:
                chunks = search(item["question"])
                answer_text = ""
                covered = None
            else:
                result = answer_question(item["question"])
                chunks = result.chunks
                answer_text = result.text
                covered = result.covered
        latency_ms = round((time.perf_counter() - asked_at) * 1000)

        sources = [c.source_path for c in chunks]
        hit = wanted in sources
        hit_at_1 = bool(sources) and sources[0] == wanted
        rank = sources.index(wanted) + 1 if hit else None

        record = {
            "id": item["id"],
            "type": item["type"],
            "question": item["question"],
            "expected_doc": item["expected_doc"],
            "retrieved_docs": sources,
            "retrieval_hit": hit,
            "retrieval_hit_at_1": hit_at_1,
            "rank_of_expected": rank,
            "answer": answer_text,
            "covered": covered,
            "latency_ms": latency_ms,
            "system_usage": system_usage.to_dict(),
        }

        if judged and answer_text:
            if answer_text.strip().upper() == NOT_COVERED:
                record["faithful"] = True
                record["unsupported_claims"] = []
                record["correct"] = False
                record["correctness_reason"] = "declined to answer an answerable question"
            else:
                with track() as judge_usage:
                    faithful, claims = judge_faithfulness(build_context(chunks), answer_text)
                    correct, reason = judge_correctness(
                        item["question"], item["reference_answer"], answer_text
                    )
                record["judge_cost_usd"] = round(judge_usage.cost_usd, 6)
                record["faithful"] = faithful
                record["unsupported_claims"] = claims
                record["correct"] = correct
                record["correctness_reason"] = reason

        records.append(record)
        flag = "hit " if hit else "MISS"
        extra = ""
        if "correct" in record:
            extra = f"  correct={'Y' if record['correct'] else 'N'}  faithful={'Y' if record['faithful'] else 'N'}"
        print(f"  [{position:>2}/{len(items)}] {item['id']}  {flag} rank={rank or '-':<3}{extra}")

    elapsed = time.time() - started
    return summarise(records, elapsed, judged)


def _rate(records: list[dict], key: str) -> float | None:
    present = [r for r in records if key in r and r[key] is not None]
    if not present:
        return None
    return sum(1 for r in present if r[key]) / len(present)


def percentile(values: list[float], share: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    index = min(len(ordered) - 1, round(share * (len(ordered) - 1)))
    return ordered[index]


def usage_block(records: list[dict]) -> dict:
    """What the system cost to run, per question, with the judges kept out."""
    latencies = [r["latency_ms"] for r in records]
    system_cost = sum(r["system_usage"]["cost_usd"] for r in records)
    judge_cost = sum(r.get("judge_cost_usd", 0.0) for r in records)
    n = len(records) or 1
    return {
        "latency_ms_p50": percentile(latencies, 0.50),
        "latency_ms_p95": percentile(latencies, 0.95),
        "cost_usd_per_question": round(system_cost / n, 6),
        "system_cost_usd": round(system_cost, 6),
        "judge_cost_usd": round(judge_cost, 6),
        "cost_usd": round(system_cost + judge_cost, 6),
        "input_tokens": sum(r["system_usage"]["input_tokens"] for r in records),
        "output_tokens": sum(r["system_usage"]["output_tokens"] for r in records),
    }


def summarise(records: list[dict], elapsed: float, judged: bool) -> dict:
    by_type: dict[str, list[dict]] = defaultdict(list)
    for record in records:
        by_type[record["type"]].append(record)

    def block(rows: list[dict]) -> dict:
        ranks = [r["rank_of_expected"] for r in rows if r["rank_of_expected"]]
        return {
            "n": len(rows),
            "retrieval_hit_rate": _rate(rows, "retrieval_hit"),
            "retrieval_hit_rate_at_1": _rate(rows, "retrieval_hit_at_1"),
            "mean_rank_when_hit": round(sum(ranks) / len(ranks), 2) if ranks else None,
            "faithfulness": _rate(rows, "faithful"),
            "correctness": _rate(rows, "correct"),
            "abstention_rate": (
                sum(1 for r in rows if r.get("covered") is False) / len(rows)
                if rows and rows[0].get("covered") is not None else None
            ),
        }

    return {
        "config": {
            "provider": settings.provider,
            "chat_model": settings.chat_model,
            "embedding_model": settings.embedding_model,
            "vector_top_k": settings.vector_top_k,
            "keyword_top_k": settings.keyword_top_k,
            "rerank_top_k": settings.rerank_top_k,
            "reranking": settings.reranking_enabled,
            "judged": judged,
        },
        "overall": block(records),
        "by_type": {name: block(rows) for name, rows in sorted(by_type.items())},
        "usage": usage_block(records),
        "seconds": round(elapsed, 1),
        "records": records,
    }


def print_report(summary: dict) -> None:
    def pct(value: float | None) -> str:
        return "  n/a" if value is None else f"{value * 100:5.1f}%"

    config = summary["config"]
    print("\n" + "=" * 72)
    print("KNOWLEDGE SERVICE EVALUATION")
    print("=" * 72)
    print(f"Provider {config['provider']}  |  chat {config['chat_model']}  |  "
          f"embed {config['embedding_model']}")
    print(f"Retrieval: vector top {config['vector_top_k']}, keyword top "
          f"{config['keyword_top_k']}, rerank to {config['rerank_top_k']}")
    if not config["judged"]:
        print("\nNOTE: faithfulness and correctness need a real model and were not")
        print("      scored in this run. Retrieval numbers below are still valid.")

    overall = summary["overall"]
    print(f"\n{'':<16}{'n':>4}{'hit':>8}{'hit@1':>8}{'faithful':>10}{'correct':>9}{'abstain':>9}")
    print("-" * 72)
    for name, block in summary["by_type"].items():
        print(f"{name:<16}{block['n']:>4}{pct(block['retrieval_hit_rate']):>8}"
              f"{pct(block['retrieval_hit_rate_at_1']):>8}{pct(block['faithfulness']):>10}"
              f"{pct(block['correctness']):>9}{pct(block['abstention_rate']):>9}")
    print("-" * 72)
    print(f"{'OVERALL':<16}{overall['n']:>4}{pct(overall['retrieval_hit_rate']):>8}"
          f"{pct(overall['retrieval_hit_rate_at_1']):>8}{pct(overall['faithfulness']):>10}"
          f"{pct(overall['correctness']):>9}{pct(overall['abstention_rate']):>9}")
    print(f"\nMean rank of the expected document when found: "
          f"{overall['mean_rank_when_hit']}")
    usage = summary["usage"]
    print(f"Latency per question: p50 {usage['latency_ms_p50']} ms, "
          f"p95 {usage['latency_ms_p95']} ms")
    print(f"Cost: ${usage['cost_usd_per_question']:.5f} per question, "
          f"${usage['cost_usd']:.4f} for this run including judges")
    print(f"Completed in {summary['seconds']}s")

    misses = [r for r in summary["records"] if not r["retrieval_hit"]]
    if misses:
        print(f"\nRetrieval misses ({len(misses)}):")
        for r in misses[:10]:
            print(f"  {r['id']}  expected {r['expected_doc']}")
            print(f"        got {', '.join(dict.fromkeys(r['retrieved_docs']))[:90]}")

    wrong = [r for r in summary["records"] if r.get("correct") is False]
    if wrong:
        print(f"\nIncorrect answers ({len(wrong)}):")
        for r in wrong[:10]:
            print(f"  {r['id']}  {r.get('correctness_reason', '')[:88]}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate the knowledge service.")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--retrieval-only", action="store_true",
                        help="Skip answer generation and judging. No model calls.")
    args = parser.parse_args()

    items = load_golden_set(args.limit)
    print(f"Evaluating {len(items)} golden questions ...")
    summary = evaluate(items, retrieval_only=args.retrieval_only)
    print_report(summary)

    EVAL_DIR.mkdir(parents=True, exist_ok=True)
    out = EVAL_DIR / "knowledge_eval.json"
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"\nFull results: {out}")


if __name__ == "__main__":
    main()
