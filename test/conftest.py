import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from faker import Faker
from digiliencia.configs.fastAPI.core.config import settings as fastapi_settings

import pytest_asyncio

from sqlalchemy import insert
import json
from digiliencia.configs.fastAPI.db.models import (
    User,
    Chat,
    Message,
    IAPrompt,
    Model,
)

faker = Faker()

# Configuration constants
TEST_DB_CONFIG = {
    # En CI (main.yml) esto vendrá inyectado como bolt://user:pass@localhost:7687
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


# --- SQL Database Setup ---
TEST_DATABASE_URL = fastapi_settings.DATABASE_TEST_URL
engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


# =============================================================================
# Database
# =============================================================================


@pytest_asyncio.fixture(scope="session")
async def setup_database():
    """
    Session-scoped fixture to initialize and tear down the test database.

    It runs once per test session, dropping and recreating all tables to ensure
    a clean state, then seeds the database with initial data. After all tests
    are finished, it drops all tables again.
    """

    # Seed data in a separate session
    async with TestingSessionLocal() as session:
        async with session.begin():
            users = [
                {
                    "email": faker.unique.email(),
                    "hashed_password": faker.password(length=12),
                }
                for _ in range(5)
            ]
            result_users = await session.execute(insert(User).returning(User.id), users)
            user_ids = [row.id for row in result_users]

            prompts = [
                {
                    "prompt_name": faker.text(max_nb_chars=100),
                    "prompt": faker.text(max_nb_chars=100),
                    "prompt_description": faker.sentence(),
                }
                for _ in range(3)
            ]
            result_prompts = await session.execute(
                insert(IAPrompt).returning(IAPrompt.id), prompts
            )
            prompt_ids = [row.id for row in result_prompts]

            chats = [
                {
                    "tittle": faker.sentence(nb_words=3),
                    "user_id": faker.random_element(user_ids),
                    "ia_prompt_id": faker.random_element(prompt_ids),
                }
                for _ in range(10)
            ]
            result_chats = await session.execute(insert(Chat).returning(Chat.id), chats)
            chat_ids = [row.id for row in result_chats]

            models_data = [{"ia_name": faker.unique.word()} for _ in range(3)]
            result_models = await session.execute(
                insert(Model).returning(Model.id), models_data
            )
            model_ids = [row.id for row in result_models]

            messages = []
            for chat_id in chat_ids:
                for order in range(1, 4):
                    messages.append(
                        {
                            "order_number": order,
                            "content": faker.paragraph(),
                            "statistics": json.dumps(
                                {"tokens": faker.random_int(1, 100)}
                            ),
                            "chat_id": chat_id,
                            "model_id": faker.random_element(model_ids),
                        }
                    )
            await session.execute(insert(Message), messages)

        await session.commit()

    yield
