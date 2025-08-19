from typing import List, Optional
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(self, model_name: str, device: Optional[str] = None):
        # SentenceTransformer gestiona el device automáticamente; se puede forzar con .to(device)
        self.model = SentenceTransformer(model_name)
        if device:
            try:
                self.model = self.model.to(device)
            except Exception:
                # Fallback silencioso si el device no es válido
                pass
        self.device = str(device) if device else "auto"

    def embed_one(self, text: str) -> List[float]:
        if text is None or not str(text).strip():
            raise ValueError("Texto vacío o nulo")
        vec = self.model.encode(text, show_progress_bar=False)
        return vec.tolist()

    def embed_many(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        # Filtrado y validación
        cleaned = [t for t in (texts or []) if isinstance(t, str) and t.strip()]
        if not cleaned:
            raise ValueError("Todos los textos están vacíos o no son válidos")
        vectors = self.model.encode(cleaned, show_progress_bar=False, normalize_embeddings=False)
        return [v.tolist() for v in vectors]
