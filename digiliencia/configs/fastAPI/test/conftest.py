# /tests/conftest.py
import pytest_asyncio
import httpx
import uuid
import time
import uvicorn
import multiprocessing
from typing import AsyncGenerator, Any
import psycopg2

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL


from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el .env del proyecto
from pathlib import Path
dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path)
from db.models import User
from db.session import Base
from main import app  # Import the FastAPI app instance


# Get DB owner credentials for test DB connection
DB_OWNER_USER = os.getenv("DB_OWNER_USER")
DB_OWNER_PASSWORD = os.getenv("DB_OWNER_PASSWORD")
APP_DB_NAME = os.getenv("APP_DB_NAME")

# Compose test DB name and URL for SQLAlchemy (asyncpg)
test_db_name = APP_DB_NAME + "_test"

TEST_DATABASE_URL = f"postgresql+asyncpg://{DB_OWNER_USER}:{DB_OWNER_PASSWORD}@localhost:5432/{test_db_name}"

# Get admin credentials for DB creation/deletion
ADMIN_USER = os.getenv("POSTGRES_USER")
ADMIN_PASSWORD = os.getenv("POSTGRES_PASSWORD")

admin_url = f"postgresql://{ADMIN_USER}:{ADMIN_PASSWORD}@localhost:5432/postgres"


engine = create_async_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

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
async def setup_database(app_server):
    """Creates the test database, tables, and drops everything after tests."""
    # Create test DB using admin connection
    # Use sync engine for DB creation (CREATE DATABASE not allowed in async)
    sync_admin_url = admin_url
    try:
        conn = psycopg2.connect(sync_admin_url)
        conn.autocommit = True  # ✅ Activa autocommit antes de usar cursor
        cur = conn.cursor()
        
        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (test_db_name,))
        exists = cur.fetchone()
        if not exists:
            cur.execute(f'CREATE DATABASE "{test_db_name}"')
        
        cur.close()
        conn.close()
    except Exception as e:
        raise RuntimeError(f"Could not create test database: {e}")

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Drop tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    # Drop test DB (must disconnect all sessions first)
    try:
        with psycopg2.connect(sync_admin_url) as conn:
            conn.autocommit = True
            with conn.cursor() as cur:
                # Terminate all connections to the test DB
                cur.execute(f"SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE datname = %s", (test_db_name,))
                cur.execute(f"DROP DATABASE IF EXISTS \"{test_db_name}\"")
    except Exception as e:
        print(f"Warning: Could not drop test database: {e}")


@pytest_asyncio.fixture(scope="function")
async def db_session(setup_database) -> AsyncGenerator[AsyncSession, None]:
    """Provides a clean database session for each test."""
    async with TestingSessionLocal() as session:
        yield session


# --- HTTP Client Fixtures ---
API_URL = "http://127.0.0.1:8000/api"


@pytest_asyncio.fixture(scope="session")
async def api_client() -> AsyncGenerator[httpx.AsyncClient, Any]:
    """Asynchronous, unauthenticated HTTP client."""
    async with httpx.AsyncClient(base_url=API_URL) as client:
        yield client


@pytest_asyncio.fixture(scope="function")
async def authenticated_client(
    api_client: httpx.AsyncClient, db_session: AsyncSession
) -> AsyncGenerator[httpx.AsyncClient, Any]:
    """
    Creates a user, logs in (custom or standard), and returns an authenticated HTTP client.
    Cleans up the user from the DB after the test.
    """
    email = f"testuser_{uuid.uuid4()}@example.com"
    password = "aVerySecurePassword123"
    user_payload = {"email": email, "password": password}

    register_response = await api_client.post("/register", json=user_payload)
    assert register_response.status_code in (200, 201)
    user_id = register_response.json().get("id")
    token = None

    # 1. Intentar login personalizado (JSON)
    login_payload_json = {"email": email, "password": password}
    login_response = await api_client.post("/auth/login", json=login_payload_json)
    if login_response.status_code == 200 and "access_token" in login_response.json():
        token = login_response.json()["access_token"]
    else:
        # 2. Intentar login estándar (form-data)
        login_payload_form = {"username": email, "password": password}
        login_response = await api_client.post(
            "/auth/jwt/login", data=login_payload_form
        )
        assert login_response.status_code == 200
        token = login_response.json()["access_token"]

    assert token, "No se pudo obtener el token de autenticación"

    auth_client = httpx.AsyncClient(
        base_url=API_URL, headers={"Authorization": f"Bearer {token}"}
    )
    yield auth_client

    await auth_client.aclose()

    if user_id:
        user_to_delete = await db_session.get(User, uuid.UUID(user_id))
        if user_to_delete:
            await db_session.delete(user_to_delete)
            await db_session.commit()
