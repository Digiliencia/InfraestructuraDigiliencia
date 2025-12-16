# /core/config.py
"""
This module defines the application's configuration settings.

It uses Pydantic's `BaseSettings` to validate and load configuration variables
from environment variables and .env files.
"""

import json
import logging
from typing import List

from dotenv import load_dotenv
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# Load environment variables from .env file explicitly
load_dotenv()


class Settings(BaseSettings):
    """
    Application settings schema.

    Centralizes all configuration (Database, Redis, Auth, CORS) and enforces
    type safety using Pydantic.
    """

    FASTAPI_HOST: str
    FASTAPI_PORT: int = 8080
    # --- Test environment flag ---
    TESTING: bool = False  # By default, not test

    # --- Local environment flag ---
    LOCAL: bool = False  # By default, not local

    @property
    def FASTAPI_URL(self) -> str:
        """
        Constructs the asynchronous PostgreSQL connection string.

        Returns:
            str: The full SQLAlchemy async connection URL.
        """
        if self.LOCAL:
            self.FASTAPI_HOST = "localhost"
        return f"http://{self.FASTAPI_HOST}:{self.FASTAPI_PORT}"

    # --- Database Configuration ---
    # Standardized names compatible with typical Docker environments
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_DB_TEST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str

    @property
    def DATABASE_URL(self) -> str:
        """
        Constructs the asynchronous PostgreSQL connection string.

        Returns:
            str: The full SQLAlchemy async connection URL.
        """
        if self.LOCAL:
            self.POSTGRES_SERVER = "localhost"
        logging.info(f"DB Server: {self.POSTGRES_SERVER}")
        if self.TESTING:
            return (
                f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB_TEST}"
            )
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # --- Redis Configuration ---
    REDIS_HOST: str
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str | None = None

    @property
    def REDIS_URL(self) -> str:
        """
        Constructs the Redis connection URL.

        Returns:
            str: The full Redis connection string.
        """
        if self.LOCAL:
            self.REDIS_HOST = "localhost"
        if self.REDIS_PASSWORD:
            return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    # --- JWT Authentication ---
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_SECONDS: int = 3600  # Default to 1 hour if not set

    # --- CORS Configuration ---
    ALLOWED_ORIGINS: List[str] = []

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def parse_allowed_origins(cls, v: str | List[str]) -> List[str]:
        """
        Parses a JSON string of allowed origins into a list.
        """
        if isinstance(v, str) and not v.startswith("["):
            # Handle comma-separated strings just in case
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, str):
            try:
                parsed = json.loads(v)
                if isinstance(parsed, list):
                    return parsed
                raise ValueError("ALLOWED_ORIGINS must be a JSON list.")
            except json.JSONDecodeError:
                raise ValueError("ALLOWED_ORIGINS is not valid JSON.")
        return v

    # --- Pydantic Configuration ---
    model_config = SettingsConfigDict(
        case_sensitive=True, env_file=".env", extra="ignore"
    )


# Global settings instance
settings = Settings()
