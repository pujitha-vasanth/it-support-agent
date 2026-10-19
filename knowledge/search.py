"""Command line entry point for a one-off question. Handy for a quick demo.

    python -m knowledge.search "how long does a VPN session last?"
    python -m knowledge.search --retrieval-only "error IVE-3105"
"""

from __future__ import annotations

import argparse

from knowledge.answer import answer_question
from knowledge.retrieval import search


def main() -> None:
    parser = argparse.ArgumentParser(description="Ask the knowledge service a question.")
    parser.add_argument("question", help="The question to ask.")
    parser.add_argument(
        "--retrieval-only",
        action="store_true",
        help="Show the retrieved chunks without calling the language model.",
    )
    parser.add_argument("--top-k", type=int, default=None, help="Chunks to keep after reranking.")
    args = parser.parse_args()

    if args.retrieval_only:
        for i, chunk in enumerate(search(args.question, top_k=args.top_k), start=1):
            score = chunk.rerank_score
            score_text = f"rerank {score:+.3f}" if score is not None else f"rrf {chunk.fused_score:.4f}"
            print(f"\n[{i}] {chunk.citation}   ({score_text}, found by {'+'.join(chunk.found_by)})")
            print(f"    {chunk.body[:300]}...")
        return

    result = answer_question(args.question, top_k=args.top_k)
    print(f"\n{result.text}\n")
    if result.chunks:
        print("Sources:")
        for citation in result.citations:
            print(f"  [{citation['n']}] {citation['document']}, {citation['section']} "
                  f"(p. {citation['page']})")


if __name__ == "__main__":
    main()
