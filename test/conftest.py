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
from typing import AsyncGenerator, Generator

from passlib.context import CryptContext
import pytest
import pytest_asyncio
from faker import Faker
from sqlalchemy import insert, text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

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
    """
    Session-scoped fixture to seed the database with initial data.

    PRECONDITION: The database containers are running and tables exist.
    This fixture connects directly to the DB to populate it before tests run.
    """

    async with engine.begin() as conn:
        await conn.execute(
            text(
                "TRUNCATE users, chats, messages, ai_prompts, models RESTART IDENTITY CASCADE;"
            )
        )

    async with TestingSessionLocal() as session:
        async with session.begin():
            # 1. Users
            users_data = [
                {
                    "email": faker.unique.email(),
                    "hashed_password": faker.password(length=12),
                    "is_active": True,
                    "is_superuser": False,
                    "is_verified": True,
                }
                for _ in range(5)
            ]
            result_users = await session.execute(
                insert(User).returning(User.id), users_data
            )
            user_ids = [row.id for row in result_users]

            # 2. AI Prompts (Templates)
            prompts_data = [
                {
                    "name": faker.unique.job(),
                    "prompt_text": faker.text(max_nb_chars=100),
                    "description": faker.sentence(),
                }
                for _ in range(3)
            ]
            result_prompts = await session.execute(
                insert(AIPrompt).returning(AIPrompt.id), prompts_data
            )
            prompt_ids = [row.id for row in result_prompts]

            # 3. Models
            models_data = [{"name": faker.unique.word()} for _ in range(3)]
            result_models = await session.execute(
                insert(Model).returning(Model.id), models_data
            )
            model_ids = [row.id for row in result_models]

            # 4. Chats
            chats_data = [
                {
                    "title": faker.sentence(nb_words=3),
                    "user_id": faker.random_element(user_ids),
                    "ai_prompt_id": faker.random_element(prompt_ids),
                }
                for _ in range(10)
            ]
            result_chats = await session.execute(
                insert(Chat).returning(Chat.id), chats_data
            )
            chat_ids = [row.id for row in result_chats]

            # 5. Messages
            messages_data = []
            for chat_id in chat_ids:
                for order in range(1, 4):
                    messages_data.append(
                        {
                            "order_number": order,
                            "content": faker.paragraph(),
                            "statistics": {"tokens": faker.random_int(1, 100)},
                            "chat_id": chat_id,
                            "model_id": faker.random_element(model_ids),
                        }
                    )
            await session.execute(insert(Message), messages_data)

        await session.commit()

    yield


@pytest_asyncio.fixture(scope="function")
async def db_session(setup_database) -> AsyncGenerator[AsyncSession, None]:
    """
    Function-scoped fixture that provides a direct database session for
    verification within tests (if needed).
    """
    async with TestingSessionLocal() as session:
        yield session
