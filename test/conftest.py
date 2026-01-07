# tests/conftest.py
"""
Global Pytest Configuration.

This module sets up the test environment assuming:
1. The Database is accessible directly for seeding (via SQLAlchemy).
2. The API is ALREADY RUNNING externally (e.g., in Docker or Uvicorn).
   The tests will act as a real HTTP client connecting to it.
"""

import asyncio
import os
from typing import Generator
import logging

from passlib.context import CryptContext
import pytest
import pytest_asyncio
from faker import Faker
from sqlalchemy import insert, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import random

from digiliencia.configs.fastAPI.core.config import settings as fastapi_settings

# Import updated models
from digiliencia.configs.fastAPI.db.models import (
    User,
    Chat,
    Message,
    AIPrompt,
    Model,
)

faker = Faker()

# =============================================================================
# Configuration Constants
# =============================================================================

TEST_DB_CONFIG = {
    "DDBB_URI": os.getenv("DDBB_URI", "bolt://neo4j:testpassword@neo4j-test:7687"),
    "TESTING": os.getenv("TESTING", "true"),
    "WEFORUM_EMAIL": os.getenv("WEFORUM_EMAIL", "test@example.com"),
    "WEFORUM_PASSWD": os.getenv("WEFORUM_PASSWD", "testpassword"),
    "WEBDRIVERWAIT_TIMEOUT": os.getenv("WEBDRIVERWAIT_TIMEOUT", "5"),
    "IMPLICIT_WAIT": os.getenv("IMPLICIT_WAIT", "2"),
    "LLM_URL": os.getenv("LLM_URL", "http://localhost:11434"),
    "CLASSIFICATION_MODEL": os.getenv("CLASSIFICATION_MODEL", "test_model"),
    "EMBEDDINGS_SERVICE": os.getenv("EMBEDDINGS_SERVICE", "http://localhost:8000"),
    "EMBEDDINGS_PROVIDER": os.getenv("EMBEDDINGS_PROVIDER", "custom"),
    "EMBEDDINGS_MODEL": os.getenv("EMBEDDINGS_MODEL", "test_model"),
    "EMBEDDINGS_DIMENSION": os.getenv("EMBEDDINGS_DIMENSION", "4096"),
    "COMPOSE_PROJECT_DIR": os.getenv("COMPOSE_PROJECT_DIR", "../.devcontainer"),
    "SERVICE_NAME": os.getenv("SERVICE_NAME", "embedding-api-service"),
}

# =============================================================================
# Database Setup
# =============================================================================

# Engine for Direct DB Seeding
engine = create_async_engine(fastapi_settings.DATABASE_URL, echo=False, future=True)
logging.info(f"Database URL: {fastapi_settings.DATABASE_URL}")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    """
    Creates an instance of the default event loop for the test session.
    """
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def setup_database():
    async with engine.begin() as conn:
        await conn.execute(
            text("TRUNCATE users, chats, messages, ai_prompts, models CASCADE;")
        )

    async with TestingSessionLocal() as session:
        async with session.begin():
            # ------------------------------------------------------------------
            # 2. AI Models
            # ------------------------------------------------------------------
            models_list = ["GPT-4", "Claude-3", "Llama-3", "Mistral-Large"]
            models_data = [{"name": name} for name in models_list]

            result_models = await session.execute(
                insert(Model).returning(Model.id), models_data
            )
            # Guardamos los IDs para asignarlos a los mensajes luego
            model_ids = [row.id for row in result_models.all()]

            # ------------------------------------------------------------------
            # 3. AI Prompts
            # ------------------------------------------------------------------
            prompts_data = [
                {
                    "name": "General Assistant",
                    "prompt_text": "You are a helpful AI assistant.",
                    "description": "Standard assistant.",
                },
                {
                    "name": "Code Expert",
                    "prompt_text": "You are a Python expert. Write clean code.",
                    "description": "Programming helper.",
                },
                {
                    "name": "Translator",
                    "prompt_text": "Translate the following text to Spanish.",
                    "description": "English to Spanish translator.",
                },
            ]
            for _ in range(2):
                prompts_data.append(
                    {
                        "name": faker.unique.job(),
                        "prompt_text": faker.paragraph(),
                        "description": faker.sentence(),
                    }
                )

            result_prompts = await session.execute(
                insert(AIPrompt).returning(AIPrompt.id), prompts_data
            )
            prompt_ids = [row.id for row in result_prompts.all()]

            # ------------------------------------------------------------------
            # 4. Users
            # ------------------------------------------------------------------
            users_data = [
                {
                    "email": "test@example.com",
                    "hashed_password": "hashed_secret_password",
                    "is_active": True,
                    "is_superuser": False,
                    "is_verified": True,
                },
                {
                    "email": "admin@example.com",
                    "hashed_password": "hashed_admin_password",
                    "is_active": True,
                    "is_superuser": True,
                    "is_verified": True,
                },
            ]
            for _ in range(8):
                users_data.append(
                    {
                        "email": faker.unique.email(),
                        "hashed_password": faker.sha256(),
                        "is_active": faker.boolean(chance_of_getting_true=90),
                        "is_superuser": False,
                        "is_verified": faker.boolean(chance_of_getting_true=80),
                    }
                )

            result_users = await session.execute(
                insert(User).returning(User.id), users_data
            )
            user_ids = [row.id for row in result_users.all()]

            # ------------------------------------------------------------------
            # 5. Chats
            # ------------------------------------------------------------------
            chats_data = []
            for _ in range(20):
                chats_data.append(
                    {
                        "title": faker.sentence(nb_words=4).replace(".", ""),
                        "user_id": random.choice(user_ids),
                        "ai_prompt_id": random.choice(prompt_ids),
                    }
                )

            result_chats = await session.execute(
                insert(Chat).returning(Chat.id), chats_data
            )
            chat_ids = [row.id for row in result_chats.all()]

            # ------------------------------------------------------------------
            # 6. Messages
            # ------------------------------------------------------------------
            messages_data = []

            for chat_id in chat_ids:
                num_messages = random.randint(2, 6)

                for order in range(1, num_messages + 1):
                    is_ai_response = order % 2 == 0

                    msg_content = (
                        faker.paragraph() if is_ai_response else faker.sentence()
                    )
                    assigned_model = (
                        random.choice(model_ids) if is_ai_response else None
                    )

                    messages_data.append(
                        {
                            "order_number": order,
                            "content": msg_content,
                            "statistics": {
                                "tokens_in": random.randint(10, 50),
                                "tokens_out": random.randint(50, 200),
                                "latency_ms": random.randint(100, 1500),
                            },
                            "chat_id": chat_id,
                            "model_id": assigned_model,
                        }
                    )

            if messages_data:
                await session.execute(insert(Message), messages_data)

        await session.commit()

    yield
    # async with engine.begin() as conn:
    #     await conn.execute(text("TRUNCATE users, chats, messages, ai_prompts, models CASCADE;"))
