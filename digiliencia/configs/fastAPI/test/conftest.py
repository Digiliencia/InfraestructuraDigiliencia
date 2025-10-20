# /tests/conftest.py
"""
This module serves as the central configuration file for pytest.

It defines shared fixtures that are used across multiple test files to provide
dependencies like a running API server, database sessions, and HTTP clients.
This approach promotes code reuse and ensures a consistent testing environment.
"""

import pytest
import pytest_asyncio
import httpx
import time
import uvicorn
import multiprocessing
import asyncio
from typing import AsyncGenerator, Any
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert, text
from faker import Faker
import json
from httpx import AsyncClient

from pathlib import Path
import sys

from dotenv import load_dotenv

sys.path.append(str(Path(__file__).resolve().parent.parent))
from main import app
from core.config import settings
from db.models import User, Chat, Message, IAPrompt, Model, Base
from starlette import status


# Load environment variables from the project's .env file
dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path)

# --- Database Setup ---
TEST_DATABASE_URL = settings.DATABASE_URL
engine = create_async_engine(TEST_DATABASE_URL, echo=False)
TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

faker = Faker()

# --- HTTP Client Fixtures ---
API_URL = "http://127.0.0.1:8000/api"
HEALTH_CHECK_URL = "http://127.0.0.1:8000/health"


def run_server():
    """Target function to run the Uvicorn server in a separate process."""
    uvicorn.run(app, host="127.0.0.1", port=8000)


async def wait_for_server(url: str, timeout: int = 10):
    """Polls the health check endpoint until the server is responsive."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            async with httpx.AsyncClient() as client:
                await client.get(url)
                return
        except httpx.ConnectError:
            await asyncio.sleep(0.1)
    raise TimeoutError("Test server did not start within the timeout period.")


@pytest.fixture(scope="session", autouse=True)
def app_server():
    """
    Session-scoped fixture to manage the lifecycle of the FastAPI test server.

    It starts the server in a separate process before any tests run and
    terminates it after all tests in the session are complete.
    """
    proc = multiprocessing.Process(target=run_server, daemon=True)
    proc.start()
    try:
        asyncio.run(wait_for_server(HEALTH_CHECK_URL))
    except TimeoutError as e:
        proc.terminate()
        proc.join()
        pytest.fail(f"Server failed to start: {e}")

    yield

    proc.terminate()
    proc.join()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database():
    """
    Session-scoped fixture to initialize and tear down the test database.

    It runs once per test session, dropping and recreating all tables to ensure
    a clean state, then seeds the database with initial data. After all tests
    are finished, it drops all tables again.
    """
    sql_drop_tables = text(
        """
        DO $$
        BEGIN
           DROP TABLE IF EXISTS MESSAGES CASCADE;
           DROP TABLE IF EXISTS CHATS CASCADE;
           DROP TABLE IF EXISTS USERS CASCADE;
           DROP TABLE IF EXISTS IA_PROMPTS CASCADE;
           DROP TABLE IF EXISTS MODELS CASCADE;
        END $$;
        """
    )

    async with engine.begin() as conn:
        await conn.execute(sql_drop_tables)
        await conn.run_sync(Base.metadata.create_all)

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

    async with engine.begin() as conn:
        await conn.execute(sql_drop_tables)


@pytest_asyncio.fixture(scope="function")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Function-scoped fixture providing an isolated database session for each test.

    It begins a transaction before yielding the session to the test and rolls
    back the transaction after the test completes, ensuring test isolation.
    """
    async with TestingSessionLocal() as session:
        trans = await session.begin()
        try:
            yield session
        finally:
            await trans.rollback()


@pytest_asyncio.fixture(scope="function")
async def api_client() -> AsyncGenerator[httpx.AsyncClient, Any]:
    """
    Function-scoped fixture providing an unauthenticated HTTP client.
    """
    async with httpx.AsyncClient(base_url=API_URL) as client:
        yield client


@pytest.fixture(scope="function")
def fake_user() -> dict:
    """
    Function-scoped fixture that generates a dictionary with fake user data.
    """
    return {"email": faker.email(), "password": "ValidPassword123"}


@pytest_asyncio.fixture(scope="function")
async def authenticated_client(
    fake_user: dict,
) -> AsyncGenerator[httpx.AsyncClient, Any]:
    """
    Function-scoped fixture that provides an authenticated HTTP client.

    It performs the complete authentication flow:
    1. Registers a new user with fake data.
    2. Logs the new user in to obtain a JWT.
    3. Yields an HTTP client with the `Authorization` header pre-set.
    4. Deletes the user after the test is complete for cleanup.
    """
    async with httpx.AsyncClient(base_url=API_URL) as auth_client:
        response = await auth_client.post("/register", json=fake_user)
        if response.status_code != 201:
            raise Exception(f"User registration failed in fixture: {response.text}")

        response = await auth_client.post(
            "/auth/login",
            json={"email": fake_user["email"], "password": fake_user["password"]},
        )
        if response.status_code != 200:
            raise Exception(f"User login failed in fixture: {response.text}")

        token = response.json()["access_token"]
        auth_client.headers.update({"Authorization": f"Bearer {token}"})

        yield auth_client

        response = await auth_client.delete("/users/me")
        if response.status_code != 204:
            print(f"Warning: Failed to cleanup user {fake_user['email']}")


@pytest_asyncio.fixture(scope="function")
async def templates(authenticated_client: AsyncClient) -> list:
    """
    Function-scoped fixture that fetches the list of available prompt templates.
    """
    response = await authenticated_client.get("/chats/template_list")
    if response.status_code != status.HTTP_202_ACCEPTED:
        raise Exception(f"Error getting templates: {response.status_code}")

    templates_list = response.json()
    if not templates_list:
        raise Exception("No templates found in database to use in tests.")

    return templates_list


@pytest_asyncio.fixture(scope="function")
async def models(authenticated_client: AsyncClient) -> list:
    """
    Function-scoped fixture that fetches the list of available AI models.
    """
    response = await authenticated_client.get("/chats/model_list")
    if response.status_code != status.HTTP_202_ACCEPTED:
        raise Exception(f"Error getting models: {response.status_code}")

    models_list = response.json()
    if not models_list:
        raise Exception("No models found in database to use in tests.")

    return models_list
