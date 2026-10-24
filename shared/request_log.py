"""Write one row per model-backed request, and read them back as metrics.

Logging must never break the request it is logging, so a failed insert is
printed and swallowed rather than raised.
"""

from __future__ import annotations

from shared.config import settings
from shared.db import get_connection
from shared.usage import Usage


def log_request(endpoint: str, latency_ms: int, usage: Usage, outcome: str) -> None:
    try:
        with get_connection() as conn:
            conn.execute(
                """
                INSERT INTO request_log
                    (endpoint, provider, model, latency_ms, input_tokens,
                     output_tokens, cost_usd, outcome)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    endpoint,
                    settings.provider,
                    settings.chat_model,
                    latency_ms,
                    usage.input_tokens + usage.embedding_tokens,
                    usage.output_tokens,
                    usage.cost_usd,
                    outcome,
                ),
            )
    except Exception as exc:  # noqa: BLE001
        print(f"request_log insert failed: {exc}")


def metrics(hours: int = 24) -> dict:
    """Totals and percentiles over the last `hours`, overall and per endpoint."""
    with get_connection() as conn:
        rows = conn.execute(
            """
            SELECT endpoint,
                   count(*),
                   percentile_cont(0.5)  WITHIN GROUP (ORDER BY latency_ms),
                   percentile_cont(0.95) WITHIN GROUP (ORDER BY latency_ms),
                   avg(cost_usd),
                   sum(cost_usd),
                   avg((outcome = 'not_covered')::int),
                   avg((outcome = 'auto_resolvable')::int),
                   avg((outcome = 'error')::int)
            FROM request_log
            WHERE created_at > now() - make_interval(hours => %s)
            GROUP BY endpoint
            ORDER BY endpoint
            """,
            (hours,),
        ).fetchall()

        hourly = conn.execute(
            """
            SELECT date_trunc('hour', created_at) AS hour, count(*),
                   percentile_cont(0.5) WITHIN GROUP (ORDER BY latency_ms)
            FROM request_log
            WHERE created_at > now() - make_interval(hours => %s)
            GROUP BY hour ORDER BY hour
            """,
            (hours,),
        ).fetchall()

    def num(value, digits=1):
        return None if value is None else round(float(value), digits)

    endpoints = {
        row[0]: {
            "requests": row[1],
            "latency_ms_p50": num(row[2], 0),
            "latency_ms_p95": num(row[3], 0),
            "avg_cost_usd": num(row[4], 6),
            "total_cost_usd": num(row[5], 4),
            "not_covered_rate": num(row[6], 3),
            "auto_resolvable_rate": num(row[7], 3),
            "error_rate": num(row[8], 3),
        }
        for row in rows
    }
    return {
        "window_hours": hours,
        "provider": settings.provider,
        "chat_model": settings.chat_model,
        "requests": sum(e["requests"] for e in endpoints.values()),
        "total_cost_usd": round(sum(e["total_cost_usd"] or 0 for e in endpoints.values()), 4),
        "endpoints": endpoints,
        "hourly": [
            {"hour": row[0].isoformat(), "requests": row[1], "latency_ms_p50": num(row[2], 0)}
            for row in hourly
        ],
    }


def spent_today_usd() -> float:
    with get_connection() as conn:
        row = conn.execute(
            "SELECT coalesce(sum(cost_usd), 0) FROM request_log "
            "WHERE created_at >= date_trunc('day', now())"
        ).fetchone()
    return float(row[0]) if row else 0.0
