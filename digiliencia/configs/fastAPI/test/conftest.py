# /tests/conftest.py
import pytest_asyncio
import httpx
import uuid
import time
import uvicorn
import multiprocessing
from typing import AsyncGenerator, Any
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent.parent))

import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el .env del proyecto
dotenv_path = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path)

from core.config import settings
from db.models import User
from db.session import Base
from main import app  # Import the FastAPI app instance

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

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    # Optional population hook: implement to insert test data into DB
    try:
        await populate_test_data()
    except NameError:
        # populate_test_data not provided by tests; skip
        pass
    yield
    # Drop tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest_asyncio.fixture(scope="function")
async def db_session(setup_database) -> AsyncGenerator[AsyncSession, None]:
    """Provides a clean database session for each test."""
    async with TestingSessionLocal() as session:
        yield session


async def populate_test_data():
    """Default no-op population hook. Tests can monkeypatch/override this function
    (or import and call a custom implementation) to seed required data.
    """
    return


# --- HTTP Client Fixtures ---
API_URL = "http://127.0.0.1:8000/api"


@pytest_asyncio.fixture(scope="session")
async def api_client() -> AsyncGenerator[httpx.AsyncClient, Any]:
    """Asynchronous, unauthenticated HTTP client."""
    async with httpx.AsyncClient(base_url=API_URL) as client:
        yield client
