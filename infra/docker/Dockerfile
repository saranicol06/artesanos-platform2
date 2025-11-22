FROM python:3.10-slim

# Evitar prompts y mensajes
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY src/backend/requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y --no-install-recommends gcc build-essential && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y gcc build-essential && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

COPY src/backend /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
