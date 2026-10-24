"""Database helpers shared by both projects.

One connection factory, one schema initialiser. Nothing else talks to psycopg
directly, so if you ever move from local Docker to Azure Postgres or Supabase
you change DATABASE_URL in .env and nothing else.
"""

from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

import psycopg
from pgvector.psycopg import register_vector

from shared.config import settings

SCHEMA_PATH = Path(__file__).resolve().parent / "schema.sql"

_extension_ready = False


def _ensure_vector_extension(conn: psycopg.Connection) -> None:
    """A brand-new database does not have pgvector switched on yet, and the
    type adapters below cannot register until it is. Switch it on once per
    process, before anything else touches the connection."""
    global _extension_ready
    if _extension_ready:
        return
    conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
    conn.commit()
    _extension_ready = True


@contextmanager
def get_connection() -> Iterator[psycopg.Connection]:
    """Open a connection with the pgvector type adapters registered.

    Used as:  with get_connection() as conn: ...
    Commits on clean exit, rolls back if the block raises.
    """
    conn = psycopg.connect(settings.database_url)
    try:
        _ensure_vector_extension(conn)
        register_vector(conn)
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_schema() -> None:
    """Create tables and indexes if they are not already there. Safe to re-run."""
    sql = SCHEMA_PATH.read_text(encoding="utf-8").replace(
        "{EMBEDDING_DIM}", str(settings.embedding_dimensions)
    )
    with get_connection() as conn:
        conn.execute(sql)


def reset_schema() -> None:
    """Drop everything and recreate. Destructive, used by `make reset`."""
    with get_connection() as conn:
        conn.execute(
            "DROP TABLE IF EXISTS request_log, triage_runs, chunks, documents, assets CASCADE;"
        )
    init_schema()


def check_connection() -> str:
    """Return the server version, or raise a readable error."""
    try:
        with get_connection() as conn:
            row = conn.execute("SELECT version()").fetchone()
            return row[0] if row else "unknown"
    except psycopg.OperationalError as exc:
        raise RuntimeError(
            "Could not reach Postgres.\n"
            f"  Tried: {settings.database_url}\n"
            "  Is the database running? Start it with:  docker compose up -d\n"
            f"  Original error: {exc}"
        ) from exc


def table_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    with get_connection() as conn:
        for table in ("documents", "chunks", "assets", "triage_runs", "request_log"):
            try:
                row = conn.execute(f"SELECT count(*) FROM {table}").fetchone()
                counts[table] = int(row[0]) if row else 0
            except psycopg.errors.UndefinedTable:
                conn.rollback()
                counts[table] = -1
    return counts
