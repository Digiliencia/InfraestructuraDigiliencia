from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_name: str = "Qwen/Qwen3-Embedding-0.6B"
    device: str | None = None  # "cpu", "cuda", "cuda:0"

    model_config = SettingsConfigDict(env_prefix="EMBEDDINGS_", env_file=".env", extra="ignore")
