"""Hybrid retrieval: dense vectors and lexical search, fused, then reranked.

Why all three stages:

  Vector search    finds chunks that mean the same thing in different words.
                   It is weak on exact tokens like an error code.
  Keyword search   finds exact tokens. Postgres full text search handles this
                   with the tsvector column already on the chunks table, so
                   there is no second search engine to run.
  RRF fusion       merges the two ranked lists without needing the two scores
                   to be on a comparable scale, which they are not.
  Reranking        a cross-encoder reads the query and each candidate together
                   and scores relevance properly. It is slow, so it only ever
                   sees the fused shortlist, never the whole corpus.

Set RERANK_TOP_K=0 in .env to skip the final stage and avoid the PyTorch
dependency entirely.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import lru_cache

from shared.config import settings
from shared.db import get_connection
from shared.providers import get_provider

RRF_K = 60  # the usual constant; dampens the influence of the very top ranks


@dataclass
class RetrievedChunk:
    chunk_id: int
    document_id: int
    source_path: str
    title: str
    section: str
    page_approx: int
    content: str
    owner: str = ""
    vector_rank: int | None = None
    keyword_rank: int | None = None
    fused_score: float = 0.0
    rerank_score: float | None = None
    found_by: list[str] = field(default_factory=list)

    @property
    def citation(self) -> str:
        return f"{self.title}, {self.section} (p. {self.page_approx})"

    @property
    def body(self) -> str:
        """Content without the '[Title > Section]' prefix added at chunk time."""
        return re.sub(r"^\[[^\]]*\]\n", "", self.content)


def _row_to_chunk(row: tuple) -> RetrievedChunk:
    return RetrievedChunk(
        chunk_id=row[0],
        document_id=row[1],
        source_path=row[2],
        title=row[3],
        section=row[4] or "",
        page_approx=row[5] or 1,
        content=row[6],
        owner=row[7] or "",
    )


SELECT_COLUMNS = """
    c.id, c.document_id, d.source_path, d.title, c.section, c.page_approx,
    c.content, d.owner
"""


def vector_search(query: str, limit: int) -> list[RetrievedChunk]:
    """Cosine nearest neighbours. The <=> operator is pgvector's cosine distance."""
    if limit <= 0:
        return []
    embedding = get_provider().embed([query])[0]
    with get_connection() as conn:
        rows = conn.execute(
            f"""
            SELECT {SELECT_COLUMNS}
            FROM chunks c
            JOIN documents d ON d.id = c.document_id
            WHERE c.embedding IS NOT NULL
            ORDER BY c.embedding <=> %s::vector
            LIMIT %s
            """,
            (embedding, limit),
        ).fetchall()
    results = []
    for rank, row in enumerate(rows, start=1):
        chunk = _row_to_chunk(row)
        chunk.vector_rank = rank
        chunk.found_by = ["vector"]
        results.append(chunk)
    return results


_TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9\-\._/]*")


def to_or_query(query: str) -> str:
    """Build an OR-style websearch query from free text.

    Postgres treats a plain websearch query as AND, so a natural question like
    "what does error code X mean" only matches a chunk containing every word,
    and usually returns nothing. Joining the terms with OR and letting
    ts_rank_cd do the ordering is how a BM25 engine behaves, and it is what
    makes the lexical arm of this pipeline actually contribute.
    """
    tokens = [t for t in _TOKEN_RE.findall(query) if len(t) > 1]
    return " OR ".join(tokens[:40])


def keyword_search(query: str, limit: int) -> list[RetrievedChunk]:
    """Postgres full text search over the generated tsvector column.

    No second search engine is needed: the tsvector is maintained by Postgres
    on the chunks table, so lexical and vector search hit the same rows in the
    same database and stay consistent by construction.
    """
    if limit <= 0:
        return []
    tsquery = to_or_query(query)
    if not tsquery:
        return []
    with get_connection() as conn:
        rows = conn.execute(
            f"""
            SELECT {SELECT_COLUMNS}
            FROM chunks c
            JOIN documents d ON d.id = c.document_id
            WHERE c.tsv @@ websearch_to_tsquery('english', %s)
            ORDER BY ts_rank_cd(c.tsv, websearch_to_tsquery('english', %s)) DESC
            LIMIT %s
            """,
            (tsquery, tsquery, limit),
        ).fetchall()
    results = []
    for rank, row in enumerate(rows, start=1):
        chunk = _row_to_chunk(row)
        chunk.keyword_rank = rank
        chunk.found_by = ["keyword"]
        results.append(chunk)
    return results


def reciprocal_rank_fusion(
    lists: list[list[RetrievedChunk]], k: int = RRF_K
) -> list[RetrievedChunk]:
    """Merge ranked lists by summing 1/(k + rank) for each appearance.

    Scale-free, so it does not matter that cosine distance and ts_rank_cd are
    not comparable numbers.
    """
    merged: dict[int, RetrievedChunk] = {}
    for ranked in lists:
        for rank, chunk in enumerate(ranked, start=1):
            existing = merged.get(chunk.chunk_id)
            if existing is None:
                merged[chunk.chunk_id] = chunk
                existing = chunk
            else:
                existing.vector_rank = existing.vector_rank or chunk.vector_rank
                existing.keyword_rank = existing.keyword_rank or chunk.keyword_rank
                for source in chunk.found_by:
                    if source not in existing.found_by:
                        existing.found_by.append(source)
            existing.fused_score += 1.0 / (k + rank)
    return sorted(merged.values(), key=lambda c: c.fused_score, reverse=True)


@lru_cache(maxsize=1)
def _cross_encoder():
    from sentence_transformers import CrossEncoder

    return CrossEncoder(settings.rerank_model)


def rerank(query: str, candidates: list[RetrievedChunk], top_k: int) -> list[RetrievedChunk]:
    if top_k <= 0 or not candidates:
        return candidates[: max(top_k, 0)] if top_k > 0 else candidates

    try:
        model = _cross_encoder()
    except ImportError:
        print(
            "  [retrieval] sentence-transformers is not installed, so reranking "
            "was skipped. Install it, or set RERANK_TOP_K=0 in .env to silence this."
        )
        return candidates[:top_k]

    scores = model.predict([(query, c.body) for c in candidates])
    for chunk, score in zip(candidates, scores):
        chunk.rerank_score = float(score)
    return sorted(candidates, key=lambda c: c.rerank_score or 0.0, reverse=True)[:top_k]


def search(
    query: str,
    vector_k: int | None = None,
    keyword_k: int | None = None,
    top_k: int | None = None,
) -> list[RetrievedChunk]:
    """The full pipeline. This is what the API and the agent both call."""
    vector_k = settings.vector_top_k if vector_k is None else vector_k
    keyword_k = settings.keyword_top_k if keyword_k is None else keyword_k
    top_k = settings.rerank_top_k if top_k is None else top_k

    dense = vector_search(query, vector_k)
    lexical = keyword_search(query, keyword_k)
    fused = reciprocal_rank_fusion([dense, lexical])

    if top_k <= 0:
        return fused[: max(vector_k, keyword_k)]
    return rerank(query, fused, top_k)
