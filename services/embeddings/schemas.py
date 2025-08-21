from typing import List

from pydantic import BaseModel, Field


class EmbedRequest(BaseModel):
    texts: List[str] = Field(
        default_factory=list, description="Lista de textos a convertir en embeddings"
    )


class EmbedResponse(BaseModel):
    embeddings: List[List[float]]
    dim: int
