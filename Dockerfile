# ----- Base image -----
#FROM python:3.11-slim AS base
FROM public.ecr.aws/library/python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

RUN addgroup --system app && adduser --system --ingroup app app
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# ----- Dependencies layer -----
FROM base AS deps
COPY pyproject.toml .
RUN pip install --upgrade pip \
 && pip install .

# ----- Runtime image -----
FROM base AS runtime
COPY --from=deps /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=deps /usr/local/bin/gunicorn /usr/local/bin/gunicorn

COPY app.py gunicorn.conf.py ./

USER app
EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl -f http://localhost:8000/healthz || exit 1

CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]
