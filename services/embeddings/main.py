from fastapi import FastAPI, HTTPException
from .schemas import EmbedRequest, EmbedResponse
from .settings import Settings
from .service import EmbeddingService


def build_app() -> FastAPI:
    settings = Settings()
    service = EmbeddingService(model_name=settings.model_name, device=settings.device)

    app = FastAPI(title="Embeddings Service", version="0.1.0")

    @app.get("/health")
    def health():
        return {"status": "ok", "model": settings.model_name, "device": service.device}

    @app.post("/embed", response_model=EmbedResponse)
    def embed(payload: EmbedRequest):
        try:
            vectors = service.embed_many(payload.texts)
            return EmbedResponse(embeddings=vectors, dim=len(vectors[0]) if vectors else 0)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Embedding error: {e}")

    return app


app = build_app()
