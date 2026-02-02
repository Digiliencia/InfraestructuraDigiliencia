# /tests/fastApi_test/conftest.py
"""
Configuration and Fixtures for FastAPI Integration Tests (Black-box testing).

This module sets up a real Uvicorn server instance in a separate process
to allow HTTP testing against the running API endpoints via '127.0.0.1'.
"""

import asyncio
import time
from typing import Any, AsyncGenerator

import httpx
import pytest
import pytest_asyncio
from starlette import status
from httpx import AsyncClient


# Import Schema and Config
# We use the local project structure, assuming python path is set correctly
from digiliencia.configs.fastAPI.schemas.chat import Templates, Models
from digiliencia.configs.fastAPI.core.endpoints import (
    TEMPLATE_LIST,
    MODEL_LIST,
    REGISTER,
    LOGIN,
    USERS_ME,
)

from test.conftest import faker

# Constants
HOST = "127.0.0.1"
PORT = "8080"
BASE_URL = f"http://{HOST}:{PORT}/api"
HEALTH_CHECK_URL = f"{BASE_URL}/health"


# =============================================================================
# API Client
# =============================================================================


@pytest_asyncio.fixture(scope="session")
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    """
    Creates an HTTPX AsyncClient connected to the RUNNING external API.

    It does NOT spin up the FastAPI app internally. It expects the service
    to be available at API_BASE_URL.
    """
    # We simply point httpx to the external URL
    async with AsyncClient(base_url=BASE_URL) as ac:
        yield ac


# =============================================================================
# Server Process Management
# =============================================================================


async def wait_for_server(url: str, timeout: int = 10):
    """
    Polls the health check endpoint until the server is responsive.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                if response.status_code == 200:
                    return
        except (httpx.ConnectError, httpx.ReadTimeout):
            await asyncio.sleep(0.1)

    raise TimeoutError("Test server did not start within the timeout period.")


# =============================================================================
# Client Fixtures
# =============================================================================


@pytest_asyncio.fixture(scope="function")
async def api_client() -> AsyncGenerator[httpx.AsyncClient, Any]:
    """
    Provides an unauthenticated HTTP client pointing to the live test server.
    """
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        yield client


@pytest.fixture(scope="function")
def fake_user() -> dict:
    """
    Generates a dictionary with valid fake user credentials.
    """
    return {"email": faker.email(), "password": "ValidPassword123!"}


@pytest_asyncio.fixture(scope="function")
async def authenticated_client(
    fake_user: dict,
) -> AsyncGenerator[httpx.AsyncClient, Any]:
    """
    Provides an authenticated HTTP client.

    Flow:
    1. Registers a user.
    2. Logs in to get JWT.
    3. Sets Authorization header.
    4. Cleans up (deletes user) after test.
    """
    async with httpx.AsyncClient(base_url=BASE_URL) as auth_client:
        # 1. Register
        # Endpoint: /api/auth/register
        reg_response = await auth_client.post(REGISTER, json=fake_user)
        if reg_response.status_code != status.HTTP_201_CREATED:
            raise Exception(f"Registration failed: {reg_response.text}")

        # 2. Login
        # Endpoint: /api/auth/login
        login_response = await auth_client.post(
            LOGIN,
            json={"email": fake_user["email"], "password": fake_user["password"]},
        )
        if login_response.status_code != status.HTTP_200_OK:
            raise Exception(f"Login failed: {login_response.text}")

        # 3. Setup Header
        token = login_response.json()["access_token"]
        auth_client.headers.update({"Authorization": f"Bearer {token}"})

        yield auth_client

        # 4. Cleanup
        # Endpoint: /api/users/me
        del_response = await auth_client.delete(USERS_ME)
        if del_response.status_code != status.HTTP_204_NO_CONTENT:
            print(f"Warning: Failed to cleanup user {fake_user['email']}")


# =============================================================================
# Data Fetching Fixtures (Templates & Models)
# =============================================================================


@pytest_asyncio.fixture(scope="function")
async def templates(authenticated_client: httpx.AsyncClient) -> Templates:
    """
    Fetches the list of available AI templates from the API.
    """
    response = await authenticated_client.get(TEMPLATE_LIST)

    # Updated check: Changed from 202 to 200 based on new router logic
    if response.status_code != status.HTTP_200_OK:
        raise Exception(
            f"Error getting templates ({response.status_code}): {response.text}"
        )

    data = response.json()
    # Check for empty list inside the 'templates' key if necessary,
    # or the object itself depending on schema.
    # Assuming schema is: { "templates": [...] }
    if not data.get("templates"):
        raise Exception("No templates found in database (seed failed?).")

    return Templates.model_validate(data)


@pytest_asyncio.fixture(scope="function")
async def models(authenticated_client: httpx.AsyncClient) -> Models:
    """
    Fetches the list of available AI models from the API.
    """
    response = await authenticated_client.get(MODEL_LIST)

    # Updated check: Changed from 202 to 200
    if response.status_code != status.HTTP_200_OK:
        raise Exception(
            f"Error getting models ({response.status_code}): {response.text}"
        )

    data = response.json()
    # Assuming schema is: { "models": [...] }
    if not data.get("models"):
        raise Exception("No models found in database (seed failed?).")

    return Models.model_validate(data)
