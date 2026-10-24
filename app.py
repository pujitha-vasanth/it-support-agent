"""FastAPI surface for the whole system.

    uvicorn app:app --reload

Two groups of routes:

  /knowledge/*   the RAG service on its own. Useful for a demo, and it is what
                 the agent would call if you deployed the two separately.
  /agent/*       triage a ticket, then review and approve the draft.

Interactive docs at http://localhost:8000/docs once it is running.
"""

from __future__ import annotations

import time
from collections import defaultdict, deque
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field

from agent import approve as approvals
from agent.graph import run_triage
from knowledge.answer import answer_question
from knowledge.retrieval import search
from shared.config import settings
from shared.db import check_connection, init_schema, table_counts
from shared.request_log import log_request, metrics, spent_today_usd
from shared.usage import track

DASHBOARD_PATH = Path(__file__).resolve().parent / "web" / "dashboard.html"
BASELINE_PATH = Path(__file__).resolve().parent / "eval" / "baseline.json"


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Create any table that is missing (the request log, on an older
    # database). Safe to run on every start.
    try:
        init_schema()
    except Exception as exc:  # noqa: BLE001
        print(f"Schema check skipped: {exc}")
    yield


app = FastAPI(
    title="IT Support Agent",
    description="RAG knowledge service consumed as a tool by a LangGraph triage agent.",
    version="1.1.0",
    lifespan=lifespan,
)


# ---------------------------------------------------------------------------
# Guards for model-backed routes
# ---------------------------------------------------------------------------

_recent_requests: dict[str, deque] = defaultdict(deque)


def guard(request: Request) -> None:
    """Runs before every route that calls a model.

    1. Rate limit: each visitor (by IP) gets RATE_LIMIT_PER_MINUTE requests in
       any rolling minute. Kept in memory, which is right for one server.
    2. Budget: once today's logged spend passes DAILY_BUDGET_USD, model calls
       stop until midnight UTC. A public demo cannot run up a surprise bill.
    """
    visitor = request.headers.get("x-forwarded-for", "").split(",")[0].strip() or (
        request.client.host if request.client else "unknown"
    )
    now = time.monotonic()
    window = _recent_requests[visitor]
    while window and now - window[0] > 60:
        window.popleft()
    if len(window) >= settings.rate_limit_per_minute:
        raise HTTPException(status_code=429, detail="Too many requests. Try again in a minute.")
    window.append(now)

    if settings.provider != "fake" and spent_today_usd() >= settings.daily_budget_usd:
        raise HTTPException(
            status_code=429,
            detail="Today's demo budget is used up. It resets at midnight UTC.",
        )


def timed(endpoint: str, work, outcome_of):
    """Run `work`, then log its latency, tokens, cost and outcome."""
    started = time.perf_counter()
    with track() as usage:
        try:
            result = work()
        except Exception:
            log_request(endpoint, round((time.perf_counter() - started) * 1000), usage, "error")
            raise
    log_request(endpoint, round((time.perf_counter() - started) * 1000), usage, outcome_of(result))
    return result, usage


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class AskRequest(BaseModel):
    question: str = Field(..., min_length=3, examples=["How long does a VPN session last?"])
    top_k: int | None = Field(None, ge=1, le=20)


class SearchRequest(BaseModel):
    query: str = Field(..., min_length=2)
    top_k: int | None = Field(None, ge=1, le=20)


class TriageRequest(BaseModel):
    subject: str
    body: str
    requester_email: str = ""
    ticket_id: str = "AD-HOC"


class DecisionRequest(BaseModel):
    by: str = Field(..., min_length=1, description="Who is making the decision.")
    note: str = ""


# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------

@app.get("/health", tags=["health"])
def health() -> dict:
    try:
        version = check_connection().split(" on ")[0]
        counts = table_counts()
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    return {
        "status": "ok",
        "database": version,
        "provider": settings.provider,
        "chat_model": settings.chat_model,
        "embedding_model": settings.embedding_model,
        "reranking": settings.reranking_enabled,
        "counts": counts,
    }


# ---------------------------------------------------------------------------
# Knowledge service
# ---------------------------------------------------------------------------

@app.post("/knowledge/search", tags=["knowledge"], dependencies=[Depends(guard)])
def knowledge_search(request: SearchRequest) -> dict:
    """Retrieval only. Shows what the agent would be grounded on."""
    chunks, _ = timed(
        "search",
        lambda: search(request.query, top_k=request.top_k),
        lambda found: "answered" if found else "not_covered",
    )
    return {
        "query": request.query,
        "results": [
            {
                "document": c.title,
                "section": c.section,
                "page": c.page_approx,
                "found_by": c.found_by,
                "rerank_score": c.rerank_score,
                "fused_score": round(c.fused_score, 5),
                "content": c.body[:600],
            }
            for c in chunks
        ],
    }


@app.post("/knowledge/ask", tags=["knowledge"], dependencies=[Depends(guard)])
def knowledge_ask(request: AskRequest) -> dict:
    """Retrieve, then answer with citations. Returns covered=false if the
    corpus does not contain the answer, rather than guessing."""
    answer, usage = timed(
        "ask",
        lambda: answer_question(request.question, top_k=request.top_k),
        lambda a: "answered" if a.covered else "not_covered",
    )
    return {**answer.to_dict(), "usage": usage.to_dict()}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

@app.post("/agent/triage", tags=["agent"], dependencies=[Depends(guard)])
def agent_triage(request: TriageRequest) -> dict:
    """Run a ticket through the graph. Produces a draft and holds it for
    approval. Nothing is sent."""
    state, usage = timed(
        "triage",
        lambda: run_triage(request.model_dump()),
        lambda st: "auto_resolvable" if st.get("auto_resolvable") else "held",
    )
    run_id = next(
        (s.get("run_id") for s in state.get("trace", []) if s.get("node") == "persist"),
        None,
    )
    return {
        "run_id": run_id,
        "category": state.get("category"),
        "priority": state.get("priority"),
        "queue": state.get("queue"),
        "confidence": state.get("confidence"),
        "auto_resolvable": state.get("auto_resolvable"),
        "hold_reason": state.get("hold_reason"),
        "draft_reply": state.get("draft_reply"),
        "citations": state.get("citations", []),
        "asset_summary": state.get("asset_summary"),
        "trace": state.get("trace", []),
        "approval_status": "pending",
        "usage": usage.to_dict(),
    }


@app.get("/agent/runs", tags=["agent"])
def agent_runs(status: str = "pending", limit: int = 50) -> dict:
    if status not in ("pending", "approved", "rejected", "all"):
        raise HTTPException(status_code=400, detail="invalid status")
    return {"runs": approvals.list_runs(status, limit)}


@app.get("/agent/runs/{run_id}", tags=["agent"])
def agent_run(run_id: int) -> dict:
    record = approvals.get_run(run_id)
    if not record:
        raise HTTPException(status_code=404, detail=f"no run with id {run_id}")
    return record


@app.post("/agent/runs/{run_id}/approve", tags=["agent"])
def agent_approve(run_id: int, request: DecisionRequest) -> dict:
    record = approvals.decide(run_id, approvals.APPROVED, request.by, request.note)
    if not record:
        raise HTTPException(
            status_code=409,
            detail=f"run {run_id} is not pending, or does not exist",
        )
    return record


@app.post("/agent/runs/{run_id}/reject", tags=["agent"])
def agent_reject(run_id: int, request: DecisionRequest) -> dict:
    record = approvals.decide(run_id, approvals.REJECTED, request.by, request.note)
    if not record:
        raise HTTPException(
            status_code=409,
            detail=f"run {run_id} is not pending, or does not exist",
        )
    return record


# ---------------------------------------------------------------------------
# Monitoring
# ---------------------------------------------------------------------------

@app.get("/metrics", tags=["monitoring"])
def get_metrics(hours: int = 24) -> dict:
    """Live numbers from the request log: volume, latency, cost, outcomes."""
    if not 1 <= hours <= 24 * 30:
        raise HTTPException(status_code=400, detail="hours must be between 1 and 720")
    import json

    live = metrics(hours)
    live["daily_budget_usd"] = settings.daily_budget_usd
    live["spent_today_usd"] = round(spent_today_usd(), 4)
    live["quality_bar"] = json.loads(BASELINE_PATH.read_text(encoding="utf-8"))
    return live


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/dashboard", response_class=HTMLResponse, include_in_schema=False)
def dashboard() -> str:
    return DASHBOARD_PATH.read_text(encoding="utf-8")
