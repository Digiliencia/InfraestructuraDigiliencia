# /core/config.py
from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List
import json
from pathlib import Path  # 1. Importa la librería Path


# 2. Calcula la ruta raíz del proyecto (dos niveles por encima de este fichero)
#    /core/config.py -> /core/ -> /
project_root = Path(__file__).resolve().parent.parent.parent

# 3. Construye la ruta absoluta y explícita al fichero .env
dotenv_path = project_root / ".env"


class Settings(BaseSettings):
    # --- Database ---
    # Database connection parts
    DB_OWNER_USER: str
    DB_OWNER_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    APP_DB_NAME: str

    # Property that builds the full connection URL
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_OWNER_USER}:{self.DB_OWNER_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.APP_DB_NAME}"

    # --- JWT ---
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # CORS settings
    ALLOWED_ORIGINS: List[str] = []

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def validate_allowed_origins(cls, v):
        if isinstance(v, str):
            try:
                # Intentar cargar como JSON
                parsed = json.loads(v)
                if isinstance(parsed, list) and all(
                    isinstance(item, str) for item in parsed
                ):
                    return parsed
                raise ValueError("ALLOWED_ORIGINS must be a JSON list of strings")
            except json.JSONDecodeError:
                raise ValueError("ALLOWED_ORIGINS is not valid JSON")
        return v

    model_config = {
        "env_file": dotenv_path,
        "extra": "ignore",  # Ignore extra environment variables
    }


settings = Settings()
