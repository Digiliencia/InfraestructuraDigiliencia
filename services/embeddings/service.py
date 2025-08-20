from typing import List, Optional
import gc
import torch
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

    def _clear_memory(self):
        """Limpia la memoria GPU/CPU después de generar embeddings"""
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()

    def embed_one(self, text: str) -> List[float]:
        if text is None or not str(text).strip():
            raise ValueError("Texto vacío o nulo")
        try:
            vec = self.model.encode(text, show_progress_bar=False)
            result = vec.tolist()
            return result
        finally:
            # Limpiar memoria después de generar el embedding
            self._clear_memory()

    def embed_many(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        # Filtrado y validación
        cleaned = [t for t in (texts or []) if isinstance(t, str) and t.strip()]
        if not cleaned:
            raise ValueError("Todos los textos están vacíos o no son válidos")
        try:
            vectors = self.model.encode(
                cleaned, show_progress_bar=False, normalize_embeddings=False
            )
            result = [v.tolist() for v in vectors]
            return result
        finally:
            # Limpiar memoria después de generar los embeddings
            self._clear_memory()
