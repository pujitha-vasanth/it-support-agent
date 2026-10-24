"""The quality gate. Fails if any score has dropped below the saved baseline.

    python -m eval.gate              # check the latest eval results
    python -m eval.gate --update     # save the latest results as the new baseline

Run it after `make eval` (or `make eval-offline`). It reads the two result
files in eval_results/, picks the baseline profile that matches the provider
the evals ran with, and compares metric by metric.

Two kinds of rule:

  baseline     higher is better. A score may drift down by the tolerance
               (2 points by default) to absorb judge noise, but no further.
  hard limit   a fixed ceiling that never moves with the baseline. False
               auto-resolves are the failure that reaches a real user, so that
               one is capped at 5% no matter what the baseline says.

Exit code 0 means pass, 1 means a score dropped, 2 means results are missing.
GitHub Actions treats a non-zero exit as a failed check, which is what blocks
the change from being merged.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from shared.config import EVAL_DIR

BASELINE_PATH = Path(__file__).resolve().parent / "baseline.json"

# The metrics worth gating, per eval. Anything else in the results is
# reported by the eval scripts but not enforced.
GATED = {
    "knowledge": [
        "retrieval_hit_rate",
        "retrieval_hit_rate_at_1",
        "faithfulness",
        "correctness",
    ],
    "agent": [
        "category_accuracy",
        "queue_accuracy",
        "priority_within_one",
        "auto_resolve_recall",
        "asset_tool_recall",
    ],
}

LABELS = {
    "retrieval_hit_rate": "Retrieval hit rate",
    "retrieval_hit_rate_at_1": "Retrieval hit rate @1",
    "faithfulness": "Faithfulness",
    "correctness": "Correctness",
    "category_accuracy": "Category accuracy",
    "queue_accuracy": "Routing accuracy",
    "priority_within_one": "Priority within one level",
    "auto_resolve_recall": "Auto-resolve recall",
    "asset_tool_recall": "Asset tool recall",
    "false_auto_resolve_rate": "False auto-resolve rate",
}


def load_results() -> tuple[dict, dict]:
    paths = {name: EVAL_DIR / f"{name}_eval.json" for name in ("knowledge", "agent")}
    missing = [str(p) for p in paths.values() if not p.exists()]
    if missing:
        print("No eval results found. Run the evals first (make eval or make eval-offline).")
        for path in missing:
            print(f"  missing: {path}")
        sys.exit(2)
    knowledge = json.loads(paths["knowledge"].read_text(encoding="utf-8"))
    agent = json.loads(paths["agent"].read_text(encoding="utf-8"))
    return knowledge, agent


def current_scores(knowledge: dict, agent: dict) -> dict[str, dict[str, float]]:
    """Pull the gated numbers out of the two result files. A metric the run
    did not measure (faithfulness in an offline run, say) comes back as None."""
    return {
        "knowledge": {m: knowledge["overall"].get(m) for m in GATED["knowledge"]},
        "agent": {m: agent.get(m) for m in GATED["agent"] + ["false_auto_resolve_rate"]},
    }


def check(scores: dict, baseline: dict, profile: str) -> tuple[bool, list[dict]]:
    tolerance = float(baseline.get("tolerance", 0.0))
    saved = baseline["profiles"].get(profile, {})
    rows: list[dict] = []
    passed = True

    for evaluation in ("knowledge", "agent"):
        for metric, floor in saved.get(evaluation, {}).items():
            if metric.startswith("_"):
                continue
            value = scores[evaluation].get(metric)
            if value is None:
                rows.append(dict(metric=metric, value=None, rule=f">= {floor - tolerance:.2f}",
                                 status="not measured"))
                continue
            ok = value >= floor - tolerance
            passed &= ok
            rows.append(dict(metric=metric, value=value, rule=f">= {floor - tolerance:.2f}",
                             status="pass" if ok else "FAIL"))

        for metric, limit in baseline.get("hard_limits", {}).get(evaluation, {}).items():
            value = scores[evaluation].get(metric)
            if value is None:
                continue
            ok = value <= limit["max"]
            passed &= ok
            rows.append(dict(metric=metric, value=value, rule=f"<= {limit['max']:.2f} (fixed)",
                             status="pass" if ok else "FAIL"))

    return passed, rows


def render(rows: list[dict], profile: str, passed: bool, cost: float | None) -> str:
    lines = [
        f"### Quality gate: {'PASSED' if passed else 'FAILED'}",
        "",
        f"Profile: `{profile}`" + (f"  |  eval cost: ${cost:.4f}" if cost is not None else ""),
        "",
        "| Metric | Score | Rule | Result |",
        "|---|---:|---|---|",
    ]
    for r in rows:
        score = "n/a" if r["value"] is None else f"{r['value'] * 100:.1f}%"
        lines.append(f"| {LABELS.get(r['metric'], r['metric'])} | {score} | {r['rule']} | {r['status']} |")
    return "\n".join(lines)


def update_baseline(scores: dict, baseline: dict, profile: str) -> None:
    saved = baseline["profiles"].setdefault(profile, {})
    for evaluation in ("knowledge", "agent"):
        block = saved.setdefault(evaluation, {})
        for metric in GATED[evaluation]:
            value = scores[evaluation].get(metric)
            if value is not None:
                block[metric] = round(value, 4)
    BASELINE_PATH.write_text(json.dumps(baseline, indent=2) + "\n", encoding="utf-8")
    print(f"Baseline for profile '{profile}' saved to {BASELINE_PATH}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fail if any eval score dropped.")
    parser.add_argument("--update", action="store_true",
                        help="Save the latest results as the new baseline.")
    args = parser.parse_args()

    knowledge, agent = load_results()
    profile = knowledge["config"]["provider"]
    if agent["config"]["provider"] != profile:
        print("The two result files came from different providers. Re-run both evals.")
        sys.exit(2)

    baseline = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    scores = current_scores(knowledge, agent)

    if args.update:
        update_baseline(scores, baseline, profile)
        return

    costs = [r.get("usage", {}).get("cost_usd") for r in (knowledge, agent)]
    cost = sum(c for c in costs if c is not None) if any(c is not None for c in costs) else None

    passed, rows = check(scores, baseline, profile)
    if not any(r["value"] is not None for r in rows if not r["rule"].endswith("(fixed)")):
        print(f"No baseline saved yet for profile '{profile}'.")
        print("Run the evals once, check the numbers, then: python -m eval.gate --update")
    report = render(rows, profile, passed, cost)
    print(report)

    summary_file = os.getenv("GITHUB_STEP_SUMMARY")
    if summary_file:
        with open(summary_file, "a", encoding="utf-8") as handle:
            handle.write(report + "\n")

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
