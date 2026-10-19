# Shortcuts. Every one of these is a plain command you could type yourself;
# `make` just saves you remembering them. Run `make help` for the list.

.DEFAULT_GOAL := help
PY := python

help:  ## Show this list
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  %-14s %s\n", $$1, $$2}'

install:  ## Install Python dependencies into the active environment
	$(PY) -m pip install -r requirements.txt

check:  ## Check that everything is set up correctly
	$(PY) scripts/check_setup.py

db-up:  ## Start Postgres with pgvector in Docker
	docker compose up -d
	@echo "Waiting for the database to accept connections ..."
	@until docker compose exec -T db pg_isready -U itsupport -d itsupport >/dev/null 2>&1; \
		do sleep 1; done
	@echo "Database is ready."

db-down:  ## Stop the database (keeps the data)
	docker compose down

db-wipe:  ## Stop the database and delete all its data
	docker compose down -v

data:  ## Generate the corpus, golden set, tickets and asset inventory
	$(PY) -m data.generate

ingest:  ## Load the corpus into the database (use make reingest to start clean)
	$(PY) -m knowledge.ingest

reingest:  ## Drop everything and load the corpus from scratch
	$(PY) -m knowledge.ingest --reset

api:  ## Run the API at http://localhost:8000 (docs at /docs)
	$(PY) -m uvicorn app:app --reload

triage:  ## Triage all 50 sample tickets into the approval queue
	$(PY) scripts/run_tickets.py

pending:  ## List drafts waiting for a human decision
	$(PY) -m agent.approve list

eval: eval-knowledge eval-agent  ## Run both evaluations

eval-knowledge:  ## Score the knowledge service on the 50 golden questions
	$(PY) -m eval.knowledge_eval

eval-agent:  ## Score the triage agent on the 50 labelled tickets
	$(PY) -m eval.agent_eval

eval-free:  ## Retrieval-only evaluation, makes no model calls and costs nothing
	$(PY) -m eval.knowledge_eval --retrieval-only

setup: install check data ingest  ## Install, check, generate data and ingest

.PHONY: help install check db-up db-down db-wipe data ingest reingest api \
        triage pending eval eval-knowledge eval-agent eval-free setup
