import gc
from typing import Iterable, List, Optional

import torch
from sentence_transformers import SentenceTransformer


class EmbeddingService:
    def __init__(
        self,
        model_name: str,
        device: Optional[str] = None,
        batch_size: int = 16,
        dtype: str = "auto",
        normalize_embeddings: bool = False,
        dimension: Optional[int] = None,
    ):
        # Carga del modelo
        self.model = SentenceTransformer(model_name, device=device or None)

        # Dtype para reducir VRAM
        self._dtype_context = None
        if dtype and dtype != "auto":
            if dtype.lower() in ("float16", "fp16"):  # CUDA recomendado
                self._dtype = torch.float16
            elif dtype.lower() in ("bfloat16", "bf16"):
                self._dtype = torch.bfloat16
            else:
                self._dtype = torch.float32
        else:
            self._dtype = None

        self.batch_size = int(batch_size) if batch_size else 16
        self.normalize_embeddings = bool(normalize_embeddings)
        self.dimension = dimension
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")

    def _clear_memory(self):
        """Limpia la memoria GPU/CPU después de generar embeddings"""
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()

    def embed_one(self, text: str) -> List[float]:
        if text is None or not str(text).strip():
            raise ValueError("Texto vacío o nulo")
        try:
            with torch.inference_mode():
                encode_kwargs = {
                    "show_progress_bar": False,
                    "batch_size": 1,
                    "normalize_embeddings": self.normalize_embeddings,
                    "convert_to_numpy": True,
                    "device": self.device,
                }
                if self.dimension is not None:
                    encode_kwargs["truncate_dim"] = self.dimension

                if self._dtype is not None and self.device.startswith("cuda"):
                    with torch.autocast(device_type="cuda", dtype=self._dtype):
                        vec = self.model.encode(text, **encode_kwargs)
                else:
                    vec = self.model.encode(text, **encode_kwargs)
            # Asegurar que el resultado esté en CPU y como lista para liberar VRAM
            result = vec.tolist()
            return result
        finally:
            # Limpiar memoria después de generar el embedding
            self._clear_memory()

    def _batch_iter(self, items: Iterable[str], batch_size: int) -> Iterable[List[str]]:
        batch: List[str] = []
        for t in items:
            batch.append(t)
            if len(batch) >= batch_size:
                yield batch
                batch = []
        if batch:
            yield batch

    def embed_many(self, texts: List[str]) -> List[List[float]]:
        if not texts:
            return []
        # Filtrado y validación
        cleaned = [t for t in (texts or []) if isinstance(t, str) and t.strip()]
        if not cleaned:
            raise ValueError("Todos los textos están vacíos o no son válidos")
        try:
            all_vecs: List[List[float]] = []
            with torch.inference_mode():
                for batch in self._batch_iter(cleaned, self.batch_size):
                    local_bs = len(batch)
                    while True:
                        try:
                            encode_kwargs = {
                                "show_progress_bar": False,
                                "batch_size": local_bs,
                                "normalize_embeddings": self.normalize_embeddings,
                                "convert_to_numpy": True,
                                "device": self.device,
                            }
                            if self.dimension is not None:
                                encode_kwargs["truncate_dim"] = self.dimension

                            if self._dtype is not None and self.device.startswith(
                                "cuda"
                            ):
                                with torch.autocast(
                                    device_type="cuda", dtype=self._dtype
                                ):
                                    vecs = self.model.encode(
                                        batch[:local_bs], **encode_kwargs
                                    )
                            else:
                                vecs = self.model.encode(
                                    batch[:local_bs], **encode_kwargs
                                )
                            all_vecs.extend(v.tolist() for v in vecs)
                            del vecs
                            break
                        except RuntimeError as e:
                            # Manejo de OOM en CUDA
                            if "out of memory" in str(e).lower() and local_bs > 1:
                                local_bs = max(1, local_bs // 2)
                                self._clear_memory()
                                continue
                            raise
                    self._clear_memory()

            return all_vecs
        finally:
            # Limpiar memoria después de generar los embeddings
            self._clear_memory()
