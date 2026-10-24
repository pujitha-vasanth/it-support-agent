# One container for the API and dashboard. The database lives elsewhere
# (any Postgres with pgvector), set by DATABASE_URL.
#
#   docker build -t it-support-agent .
#   docker run -p 8000:8000 --env-file .env it-support-agent

FROM python:3.12-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    HF_HOME=/app/.cache/huggingface

COPY requirements.txt .
# CPU-only PyTorch keeps the image a fraction of the GPU build's size.
RUN pip install --extra-index-url https://download.pytorch.org/whl/cpu -r requirements.txt

COPY . .

# Download the reranker at build time so the first request is not slow.
RUN python -c "from sentence_transformers import CrossEncoder; CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')" \
    && chmod -R a+rwX /app

EXPOSE 8000
CMD ["python", "scripts/start.py"]
