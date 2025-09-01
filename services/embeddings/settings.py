from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_name: str = "Qwen/Qwen3-Embedding-0.6B"
    device: str | None = None  # "cpu", "cuda", "cuda:0"
    # Control de memoria/throughput
    batch_size: int = 16  # tamaño de batch para encode
    dtype: str = "auto"  # "auto" | "float16" | "bfloat16" | "float32"
    normalize_embeddings: bool = False

    model_config = SettingsConfigDict(
        env_prefix="EMBEDDINGS_", env_file=".env", extra="ignore"
    )
