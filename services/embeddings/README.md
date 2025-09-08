# Embeddings Service

Microservicio FastAPI para generar embeddings usando modelos de Hugging Face Transformers.

## Endpoints

- `GET /health`: Comprobación de estado.
- `POST /embed`: Genera embeddings para uno o varios textos.

## Ejecución local (desarrollo)

Requisitos: Dependencias listadas en `pyproject.toml` instaladas (usa `uv`/`pip`).

```
uv sync
uv run python -m services.embeddings
```

O con Uvicorn:

```
uv run uvicorn services.embeddings.main:app --host 0.0.0.0 --port 8081 --reload
```

## Variables de entorno

- `EMBEDDINGS_MODEL_NAME`: Nombre del modelo de HF (por defecto: `sentence-transformers/all-MiniLM-L6-v2`).
- `EMBEDDINGS_DEVICE`: `cpu`, `cuda`, o índice como `cuda:0` (por defecto auto).
