# /tests/conftest.py
import pytest_asyncio
import httpx
import time
import uvicorn
import multiprocessing
from typing import AsyncGenerator, Any
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import insert
from faker import Faker
import json

from pathlib import Path
import sys

from dotenv import load_dotenv

sys.path.append(str(Path(__file__).resolve().parent.parent))
from main import app  # Import the FastAPI app instance
from core.config import settings

from db.models import User, Chat, Message, IAPrompt, Model

faker = Faker()
# Cargar variables de entorno desde el .env del proyecto
dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path)


# Use original DATABASE_URL from settings (no create/drop DB)
DATABASE_URL = settings.DATABASE_URL
engine = create_async_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# --- HTTP Client Fixtures ---
API_URL = "http://127.0.0.1:8000/api"


# --- Fixture to manage the API server lifecycle ---
def run_server():
    """Function to be run in a separate process to serve the app."""
    # Note: We're running the imported 'app' instance
    uvicorn.run(app, host="127.0.0.1", port=8000)


@pytest_asyncio.fixture(scope="session", autouse=True)
def app_server():
    """Starts and stops the API server for the entire test session."""
    proc = multiprocessing.Process(target=run_server, daemon=True)
    proc.start()
    time.sleep(2)  # Give the server a moment to start
    yield
    proc.terminate()
    proc.join()


@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database(db_session: AsyncSession):
    """Populate database."""
    # USERS
    users = [
        {"email": faker.unique.email(), "hashed_password": faker.password(length=12)}
        for _ in range(5)
    ]
    result_users = await db_session.execute(insert(User).returning(User.id), users)
    user_ids = [row.id for row in result_users]

    # CHATS
    chats = [
        {
            "titulo": faker.sentence(nb_words=3),
            "user_id": faker.random_element(user_ids),
        }
        for _ in range(10)
    ]
    result_chats = await db_session.execute(insert(Chat).returning(Chat.id), chats)
    chat_ids = [row.id for row in result_chats]

    # IA_PROMPTS
    prompts = [
        {
            "prompt": faker.text(max_nb_chars=100),
            "prompt_description": faker.sentence(),
            "ia_name": faker.unique.user_name(),
        }
        for _ in range(3)
    ]
    result_prompts = await db_session.execute(
        insert(IAPrompt).returning(IAPrompt.id), prompts
    )
    prompt_ids = [row.id for row in result_prompts]

    # MODELS
    models = [{"ia_name": faker.unique.word()} for _ in range(3)]
    result_models = await db_session.execute(insert(Model).returning(Model.id), models)
    model_ids = [row.id for row in result_models]

    # MESSAGES
    messages = []
    for chat_id in chat_ids:
        for order in range(1, 4):
            messages.append(
                {
                    "order_number": order,
                    "content": faker.paragraph(),
                    "statistics": json.dumps({"tokens": faker.random_int(1, 100)}),
                    "chat_id": chat_id,
                    "model_id": faker.random_element(model_ids),
                    "ia_prompt_id": faker.random_element(prompt_ids),
                }
            )
    await db_session.execute(insert(Message), messages)


@pytest_asyncio.fixture(scope="session", autouse=False)
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Provides a clean database session for each test."""
    async with TestingSessionLocal() as session:
        trans = await session.begin()
        yield session
        await trans.commit()


@pytest_asyncio.fixture(scope="function", autouse=False)
async def api_client() -> AsyncGenerator[httpx.AsyncClient, Any]:
    """Asynchronous, unauthenticated HTTP client."""
    async with httpx.AsyncClient(base_url=API_URL) as client:
        yield client


# Faker
@pytest_asyncio.fixture
async def fake_user(scope="function", autouse=False) -> dict:
    """Generate a fake user with random email and password."""
    email = faker.email()  # Generate a random email
    password = faker.password()  # Generate a random password
    return {"email": email, "password": password}


@pytest_asyncio.fixture(scope="function", autouse=False)
async def authenticated_client(
    api_client: httpx.AsyncClient, fake_user: dict
) -> AsyncGenerator[httpx.AsyncClient, Any]:
    """Asynchronous HTTP client that is authenticated."""
    # Register the user
    response = await api_client.post("/register", json=fake_user)

    if response.status_code != 201:
        raise Exception("User registration failed in fixture authenticated_client.")

    # Log in to get the token
    response = await api_client.post("/auth/login", json=fake_user)

    if response.status_code != 200:
        raise Exception("User login failed in fixture authenticated_client.")

    token = response.json()["access_token"]

    # Set the Authorization header for future requests
    api_client.headers.update({"Authorization": f"Bearer {token}"})

    yield api_client

    response = await api_client.delete("/users/me")
    if response.status_code != 204:
        raise Exception("User delete failed in fixture authenticated_client.")
