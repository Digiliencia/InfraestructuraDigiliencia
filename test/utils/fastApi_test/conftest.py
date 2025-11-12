# /tests/fastApi_test/conftest.py
from pathlib import Path
import time

import pytest

from dotenv import load_dotenv

import pytest_asyncio
import httpx
import multiprocessing
import asyncio
from typing import AsyncGenerator, Any
from httpx import AsyncClient

from test.conftest import faker
from starlette import status
from digiliencia.configs.fastAPI.schemas.chat import Templates, Models
from digiliencia.configs.fastAPI.core.endpoints import (
    TEMPLATE_LIST,
    MODEL_LIST,
    REGISTER,
    LOGIN,
    USERS_ME,
)

# =============================================================================
# FastAPI Async SQLAlchemy Test Data Fixture
# =============================================================================

# Load environment variables from the project's .env file
dotenv_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path)

# --- HTTP Client Fixtures ---
API_URL = "http://127.0.0.1:8080/api"
HEALTH_CHECK_URL = "http://127.0.0.1:8080/api/health"


def run_server():
    """Target function to run the Uvicorn server in a separate process."""
    # uvicorn.run(app, host="127.0.0.1", port=8080)
    pass


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
def app_server(setup_database):
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
        response = await auth_client.post(REGISTER, json=fake_user)
        if response.status_code != status.HTTP_201_CREATED:
            raise Exception(f"User registration failed in fixture: {response.text}")

        response = await auth_client.post(
            LOGIN,
            json={"email": fake_user["email"], "password": fake_user["password"]},
        )
        if response.status_code != status.HTTP_200_OK:
            raise Exception(f"User login failed in fixture: {response.text}")

        token = response.json()["access_token"]
        auth_client.headers.update({"Authorization": f"Bearer {token}"})

        yield auth_client

        response = await auth_client.delete(USERS_ME)
        if response.status_code != status.HTTP_204_NO_CONTENT:
            print(f"Warning: Failed to cleanup user {fake_user['email']}")


@pytest_asyncio.fixture(scope="function")
async def templates(authenticated_client: AsyncClient) -> Templates:
    """
    Function-scoped fixture that fetches the list of available prompt templates.
    """
    response = await authenticated_client.get(TEMPLATE_LIST)
    if response.status_code != status.HTTP_202_ACCEPTED:
        raise Exception(f"Error getting templates: {response.status_code}")

    templates = response.json()
    if not templates:
        raise Exception("No templates found in database to use in tests.")

    return Templates.model_validate(templates)


@pytest_asyncio.fixture(scope="function")
async def models(authenticated_client: AsyncClient) -> Models:
    """
    Function-scoped fixture that fetches the list of available AI models.
    """
    response = await authenticated_client.get(MODEL_LIST)
    if response.status_code != status.HTTP_202_ACCEPTED:
        raise Exception(f"Error getting models: {response.status_code}")

    models = response.json()
    if not models:
        raise Exception("No models found in database to use in tests.")

    return Models.model_validate(models)
