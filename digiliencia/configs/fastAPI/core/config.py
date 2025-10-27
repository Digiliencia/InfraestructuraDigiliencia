# /core/config.py
"""
This module defines the application's configuration settings management.

It uses Pydantic's `BaseSettings` to load configuration variables from a .env
file and environment variables, providing type validation and a centralized
place for all application settings.
"""

from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List
import os
import json
from pathlib import Path


# Calculate the project's root directory (three levels up from this file)
# /core/config.py -> /core -> / -> project_root

# Build the absolute path to the .env file located at the project root.
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
if not os.path.exists(dotenv_path):
    dotenv_path = Path(__file__).resolve().parent.parent.parent.parent.parent / ".env"


class Settings(BaseSettings):
    """
    Manages all application settings, loading them from the .env file.

    This class centralizes configuration, ensuring that all required variables
    are present and correctly typed upon application startup.
    """

    # --- Database Configuration ---
    # These variables are used to construct the database connection URL.
    DB_OWNER_USER: str
    DB_OWNER_PASSWORD: str
    DB_HOST: str = "localhost"
    DB_HOST_TEST: str = "localhost"
    DB_PORT: int = 5432
    APP_DB_NAME: str

    POSTGRES_USER : str
    POSTGRES_PASSWORD : str
    APP_USER : str
    APP_USER_PASSWORD : str
    APP_USER_LOGIN : str
    APP_USER_LOGIN_PASSWORD : str

    @property
    def DATABASE_URL(self) -> str:
        """
        Constructs the full asynchronous database connection URL.

        Returns:
            str: The complete `postgresql+asyncpg` connection string.
        """
        return f"postgresql+asyncpg://{self.DB_OWNER_USER}:{self.DB_OWNER_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.APP_DB_NAME}"

    @property
    def DATABASE_TEST_URL(self) -> str:
        """
        Constructs the full asynchronous database connection URL for testing.

        Returns:
            str: The complete `postgresql+asyncpg` connection string.
        """
        return f"postgresql+asyncpg://{self.DB_OWNER_USER}:{self.DB_OWNER_PASSWORD}@{self.DB_HOST_TEST}:{self.DB_PORT}/{self.APP_DB_NAME}"

    # --- JWT Authentication ---
    # Secret key and algorithm for encoding and decoding JWTs.
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    # --- CORS (Cross-Origin Resource Sharing) ---
    # A list of origins that are allowed to make requests to the API.
    ALLOWED_ORIGINS: List[str] = []

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def validate_allowed_origins(cls, v):
        """
        Validates and parses the ALLOWED_ORIGINS setting.

        This validator allows ALLOWED_ORIGINS to be defined in the .env file
        as a JSON-formatted string (e.g., '["http://localhost:3000"]').

        Args:
            v: The raw value of ALLOWED_ORIGINS from the environment.

        Returns:
            The parsed list of origin strings.

        Raises:
            ValueError: If the string is not a valid JSON list of strings.
        """
        if isinstance(v, str):
            try:
                parsed = json.loads(v)
                if isinstance(parsed, list) and all(
                    isinstance(item, str) for item in parsed
                ):
                    return parsed
                raise ValueError("ALLOWED_ORIGINS must be a JSON list of strings")
            except json.JSONDecodeError:
                raise ValueError("ALLOWED_ORIGINS is not valid JSON")
        return v

    # Redis Configuration
    REDIS_HOST: str = "localhost"
    REDIS_HOST_TEST: str = "localhost"
    REDIS_PORT: int = 6379

    # Pydantic model configuration.
    model_config = {
        "env_file": dotenv_path,  # Specifies the path to the .env file.
        "extra": "ignore",  # Ignores any extra environment variables not defined in this model.
    }


# A global instance of the Settings class that can be imported and used
# throughout the application to access configuration values.
settings = Settings()
