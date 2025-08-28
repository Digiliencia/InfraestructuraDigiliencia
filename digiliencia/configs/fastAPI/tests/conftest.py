# /tests/conftest.py
import pytest_asyncio
import httpx
import uuid
import time
import uvicorn
import multiprocessing
from typing import Dict, AsyncGenerator, Any

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from core.config import settings
from db.models import User
from db.session import Base
from main import app # Import the FastAPI app instance

# --- Test Database Configuration ---
TEST_DATABASE_URL = f"{settings.DATABASE_URL}_test"

engine = create_async_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False, autocommit=False, autoflush=False
)

def run_server():
    """Function to be run in a separate process to serve the app."""
    uvicorn.run(app, host="127.0.0.1", port=8000)

@pytest_asyncio.fixture(scope="session", autouse=True)
def app_server():
    """Starts and stops the API server for the entire test session."""
    proc = multiprocessing.Process(target=run_server, daemon=True)
    proc.start()
    time.sleep(2) # Give the server a moment to start
    yield
    proc.terminate()
    proc.join()

@pytest_asyncio.fixture(scope="session", autouse=True)
async def setup_database(app_server):
    """Creates and tears down database tables for the test session."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

# --- HTTP Client Fixtures ---
API_URL = "http://127.0.0.1:8000/api"

@pytest_asyncio.fixture(scope="session")
async def api_client() -> AsyncGenerator[httpx.AsyncClient, Any]:
    """Asynchronous, unauthenticated HTTP client."""
    async with httpx.AsyncClient(base_url=API_URL) as client:
        yield client

@pytest_asyncio.fixture(scope="function")
async def db_session(setup_database) -> AsyncGenerator[AsyncSession, None]:
    """Provides a clean database session for each test."""
    async with TestingSessionLocal() as session:
        yield session

@pytest_asyncio.fixture(scope="function")
async def authenticated_client(api_client: httpx.AsyncClient, db_session: AsyncSession) -> AsyncGenerator[httpx.AsyncClient, Any]:
    """
    Creates a user, logs in, and returns an authenticated HTTP client.
    Cleans up the user from the DB after the test.
    """
    # 1. Register user
    email = f"testuser_{uuid.uuid4()}@example.com"
    password = "aVerySecurePassword123"
    user_payload = {"email": email, "password": password}
    
    register_response = await api_client.post("/register", json=user_payload)
    assert register_response.status_code == 201
    user_id = register_response.json()["id"]

    # 2. Log in to get the token
    login_payload = {"username": email, "password": password} # fastapi-users uses 'username'
    login_response = await api_client.post("/auth/jwt/login", data=login_payload)
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    
    # 3. Create and return the authenticated client
    auth_client = httpx.AsyncClient(
        base_url=API_URL,
        headers={"Authorization": f"Bearer {token}"}
    )
    yield auth_client
    
    # --- Teardown ---
    await auth_client.aclose()
    
    # 4. Delete the user directly from the DB to ensure a clean state
    user_to_delete = await db_session.get(User, uuid.UUID(user_id))
    if user_to_delete:
        await db_session.delete(user_to_delete)
        await db_session.commit()