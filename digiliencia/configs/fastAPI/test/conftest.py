# /tests/conftest.py
import pytest_asyncio
import httpx
import time
import uvicorn
import multiprocessing
from typing import AsyncGenerator, Any
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from faker import Faker

from pathlib import Path
import sys

from dotenv import load_dotenv

from main import app  # Import the FastAPI app instance
from core.config import settings

sys.path.append(str(Path(__file__).resolve().parent.parent))


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


# --- Fixture to create and drop the test database itself ---
@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database(db_session: AsyncSession):
    """Populate database."""
    # Populate the database. TODO: Add initial data if needed.
    yield


@pytest_asyncio.fixture(scope="session")
async def db_session() -> AsyncGenerator[AsyncSession, None]:
    """Provides a clean database session for each test."""
    async with TestingSessionLocal() as session:
        trans = await session.begin()
        try:
            yield session
        finally:
            await trans.rollback()  # To revert any changes made during the test


@pytest_asyncio.fixture(scope="function")
async def api_client() -> AsyncGenerator[httpx.AsyncClient, Any]:
    """Asynchronous, unauthenticated HTTP client."""
    async with httpx.AsyncClient(base_url=API_URL) as client:
        yield client


# Faker
@pytest_asyncio.fixture
async def fake_user(scope="function") -> dict:
    """Generate a fake user with random email and password."""
    email = Faker().email()  # Generate a random email
    password = Faker().password()  # Generate a random password
    return {"email": email, "password": password}
