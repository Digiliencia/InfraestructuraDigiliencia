# /tests/conftest.py
# CHANGED: The entire file is now async to support the async API.
import pytest_asyncio
import httpx
from typing import Dict, AsyncGenerator, Any

# --- Configuration ---
API_URL = "http://127.0.0.1:8000/api"


@pytest_asyncio.fixture(scope="session")
async def api_client() -> AsyncGenerator[httpx.AsyncClient, Any]:
    """An async client to make unauthenticated requests."""
    async with httpx.AsyncClient(base_url=API_URL) as client:
        yield client


def create_test_user(suffix: str) -> Dict[str, str]:
    """Helper to generate unique user credentials."""
    return {
        "email": f"testuser_{suffix}@example.com",
        "password": "a_very_secure_password_123",
    }


@pytest_asyncio.fixture(scope="function")
async def registered_user_factory(api_client: httpx.AsyncClient):
    """
    Async factory to register a new user.
    Yields user credentials and handles cleanup by deleting the user.
    """
    created_users = []

    async def _register_user(suffix: str):
        user_credentials = create_test_user(suffix)
        response = await api_client.post("/users/register", json=user_credentials)
        assert response.status_code == 201, "Failed to register user for test setup"

        login_response = await api_client.post("/auth/login", json=user_credentials)
        assert login_response.status_code == 200, "Failed to log in user for cleanup"

        user_data = {
            "credentials": user_credentials,
            "access_token": login_response.json()["access_token"],
            "refresh_token": login_response.json()["refresh_token"],
        }
        created_users.append(user_data)
        return user_data

    yield _register_user

    # --- Async Teardown ---
    for user in created_users:
        headers = {"Authorization": f"Bearer {user['access_token']}"}
        await api_client.delete("/users/me", headers=headers)


@pytest_asyncio.fixture(scope="function")
async def authenticated_client(registered_user_factory) -> httpx.AsyncClient:
    """An authenticated async client for User A."""
    user_data = await registered_user_factory("a")
    token = user_data["access_token"]

    auth_client = httpx.AsyncClient(
        base_url=API_URL, headers={"Authorization": f"Bearer {token}"}
    )
    yield auth_client
    await auth_client.aclose()
