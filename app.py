"""FastAPI surface for the whole system.

    uvicorn app:app --reload

Two groups of routes:

  /knowledge/*   the RAG service on its own. Useful for a demo, and it is what
                 the agent would call if you deployed the two separately.
  /agent/*       triage a ticket, then review and approve the draft.

Interactive docs at http://localhost:8000/docs once it is running.
"""

from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from agent import approve as approvals
from agent.graph import run_triage
from knowledge.answer import answer_question
from knowledge.retrieval import search
from shared.config import settings
from shared.db import check_connection, table_counts

app = FastAPI(
    title="IT Support Agent",
    description="RAG knowledge service consumed as a tool by a LangGraph triage agent.",
    version="1.0.0",
)


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

@app.post("/knowledge/search", tags=["knowledge"])
def knowledge_search(request: SearchRequest) -> dict:
    """Retrieval only. Shows what the agent would be grounded on."""
    chunks = search(request.query, top_k=request.top_k)
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


@app.post("/knowledge/ask", tags=["knowledge"])
def knowledge_ask(request: AskRequest) -> dict:
    """Retrieve, then answer with citations. Returns covered=false if the
    corpus does not contain the answer, rather than guessing."""
    return answer_question(request.question, top_k=request.top_k).to_dict()


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------

@app.post("/agent/triage", tags=["agent"])
def agent_triage(request: TriageRequest) -> dict:
    """Run a ticket through the graph. Produces a draft and holds it for
    approval. Nothing is sent."""
    state = run_triage(request.model_dump())
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
