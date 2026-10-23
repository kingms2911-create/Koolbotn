FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir anthropic requests fastapi uvicorn pillow

WORKDIR /app
COPY bot.py ./

CMD uvicorn bot:app --host 0.0.0.0 --port ${PORT:-8000}
