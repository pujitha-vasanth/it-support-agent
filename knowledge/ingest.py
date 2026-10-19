"""Load the corpus into Postgres: chunk, embed, store.

Run with:  python -m knowledge.ingest
Add --reset to wipe the existing corpus and asset tables first.

Safe to re-run. Documents are keyed by filename, so a re-run replaces a
document's chunks rather than duplicating them.
"""

from __future__ import annotations

import argparse
import csv
import time
from pathlib import Path

from shared.chunking import chunk_document, load_document
from shared.config import CORPUS_DIR, DATA_DIR, settings
from shared.db import check_connection, get_connection, init_schema, reset_schema
from shared.providers import get_provider

SUPPORTED_SUFFIXES = {".md", ".txt", ".pdf"}


def ingest_assets() -> int:
    """Load the asset inventory used by the asset-lookup sub-agent."""
    path = DATA_DIR / "assets.csv"
    if not path.exists():
        print("  no assets.csv found, skipping (run python -m data.generate first)")
        return 0

    with path.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    with get_connection() as conn:
        conn.execute("TRUNCATE assets RESTART IDENTITY")
        with conn.cursor() as cur:
            cur.executemany(
                """
                INSERT INTO assets (asset_tag, user_email, user_name, device_type,
                                    model, os_version, purchase_date, warranty_end,
                                    status, location, software)
                VALUES (%(asset_tag)s, %(user_email)s, %(user_name)s, %(device_type)s,
                        %(model)s, %(os_version)s, %(purchase_date)s, %(warranty_end)s,
                        %(status)s, %(location)s, %(software)s)
                """,
                rows,
            )
    return len(rows)


def ingest_corpus() -> tuple[int, int]:
    provider = get_provider()
    files = sorted(
        p for p in CORPUS_DIR.iterdir() if p.suffix.lower() in SUPPORTED_SUFFIXES
    )
    if not files:
        raise RuntimeError(
            f"No documents found in {CORPUS_DIR}. "
            "Run `python -m data.generate` first."
        )

    total_chunks = 0
    for position, path in enumerate(files, start=1):
        doc = load_document(path)
        chunks = chunk_document(doc)

        texts = [c.content for c in chunks]
        started = time.time()
        vectors = provider.embed(texts)
        elapsed = time.time() - started

        with get_connection() as conn:
            row = conn.execute(
                """
                INSERT INTO documents (source_path, title, doc_type, category, owner, word_count)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (source_path) DO UPDATE
                    SET title = EXCLUDED.title,
                        doc_type = EXCLUDED.doc_type,
                        category = EXCLUDED.category,
                        owner = EXCLUDED.owner,
                        word_count = EXCLUDED.word_count
                RETURNING id
                """,
                (doc.source_path, doc.title, doc.doc_type, doc.category, doc.owner, doc.word_count),
            ).fetchone()
            document_id = row[0]

            # Replace rather than append, so a re-run is idempotent.
            conn.execute("DELETE FROM chunks WHERE document_id = %s", (document_id,))
            with conn.cursor() as cur:
                cur.executemany(
                    """
                    INSERT INTO chunks
                        (document_id, chunk_index, section, page_approx, content, embedding)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """,
                    [
                        (
                            document_id,
                            c.chunk_index,
                            c.section,
                            c.page_approx,
                            c.content,
                            vector,
                        )
                        for c, vector in zip(chunks, vectors)
                    ],
                )

        total_chunks += len(chunks)
        print(
            f"  [{position:>2}/{len(files)}] {doc.title[:48]:<48} "
            f"{len(chunks):>4} chunks  {elapsed:>5.1f}s"
        )

    return len(files), total_chunks


def build_vector_index() -> None:
    """HNSW index, built after loading.

    Building it after the rows are in is noticeably faster than maintaining it
    on every insert, and on a corpus this size it takes a couple of seconds.
    """
    with get_connection() as conn:
        conn.execute("DROP INDEX IF EXISTS chunks_embedding_idx")
        conn.execute(
            "CREATE INDEX chunks_embedding_idx ON chunks "
            "USING hnsw (embedding vector_cosine_ops)"
        )
        conn.execute("ANALYZE chunks")


def main(reset: bool = False) -> None:
    print(f"Database: {check_connection().split(' on ')[0]}")
    print(f"Provider: {settings.provider}  model: {settings.embedding_model}")

    if reset:
        print("Resetting schema ...")
        reset_schema()
    else:
        init_schema()

    print("\nLoading assets ...")
    asset_count = ingest_assets()
    print(f"  {asset_count} asset records")

    print("\nLoading corpus ...")
    documents, chunks = ingest_corpus()

    print("\nBuilding vector index ...")
    build_vector_index()

    print(f"\nDone. {documents} documents, {chunks} chunks indexed.")
    print("Next step: python -m knowledge.search \"how long is a VPN session?\"")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest the corpus into Postgres.")
    parser.add_argument("--reset", action="store_true", help="Drop and recreate all tables first.")
    args = parser.parse_args()
    main(reset=args.reset)
