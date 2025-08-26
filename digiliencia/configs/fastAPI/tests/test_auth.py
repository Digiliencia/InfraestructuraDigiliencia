# /tests/test_auth.py
# CHANGED: All tests are now async. New tests for refresh tokens, password strength, and rate limiting.
import pytest
import asyncio
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_register_user_success(api_client: AsyncClient, registered_user_factory):
    """Tests successful user registration."""
    user_credentials = {
        "email": "new_user@example.com",
        "password": "a_strong_password",
    }
    response = await api_client.post("/users/register", json=user_credentials)
    assert response.status_code == 201

    # Cleanup
    login_resp = await api_client.post("/auth/login", json=user_credentials)
    token = login_resp.json()["access_token"]
    await api_client.delete("/users/me", headers={"Authorization": f"Bearer {token}"})


# NEW: Test for weak password validation
async def test_register_user_weak_password(api_client: AsyncClient):
    """Cybersecurity Test: Ensures registration fails with a weak password."""
    user_credentials = {"email": "weakpass@example.com", "password": "123"}
    response = await api_client.post("/users/register", json=user_credentials)
    assert response.status_code == 422
    assert "at least 8 characters long" in response.text


async def test_login_success(api_client: AsyncClient, registered_user_factory):
    """Tests successful login, checking for both access and refresh tokens."""
    user_data = await registered_user_factory("login_success")
    user_credentials = user_data["credentials"]

    response = await api_client.post("/auth/login", json=user_credentials)

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert "refresh_token" in data  # Check for the new refresh token
    assert data["token_type"] == "bearer"


# NEW: Test for token refresh functionality
async def test_token_refresh_success(api_client: AsyncClient, registered_user_factory):
    """Tests that a valid refresh token can be used to get a new access token."""
    # Arrange: Get initial tokens
    user_data = await registered_user_factory("refresh_success")
    refresh_token = user_data["refresh_token"]

    # Act: Use the refresh token to get new tokens
    refresh_payload = {"refresh_token": refresh_token}
    response = await api_client.post("/auth/refresh", json=refresh_payload)

    # Assert: Check for a successful response with new tokens
    assert response.status_code == 200
    new_tokens = response.json()
    assert "access_token" in new_tokens
    assert "refresh_token" in new_tokens
    assert (
        new_tokens["access_token"] != user_data["access_token"]
    )  # Ensure the token is new


async def test_token_refresh_invalid(api_client: AsyncClient):
    """Cybersecurity Test: Ensures an invalid refresh token is rejected."""
    refresh_payload = {"refresh_token": "this.is.an.invalid.token"}
    response = await api_client.post("/auth/refresh", json=refresh_payload)
    assert response.status_code == 401


# NEW: Test for rate limiting
async def test_rate_limiting_on_login(api_client: AsyncClient):
    """
    Cybersecurity Test: Verifies that the rate limiter blocks excessive requests.
    Note: This test assumes a strict limit for testing purposes (e.g., 5 per minute).
    The actual limit in `main.py` should be configured for production.
    """
    # Arrange
    user_credentials = {
        "email": "ratelimit@example.com",
        "password": "password",
    }  # Credentials don't need to be valid

    # Act: Make rapid requests until one is blocked
    for i in range(15):  # Assuming limit is less than 15
        response = await api_client.post("/auth/login", json=user_credentials)
        if response.status_code == 429:  # Too Many Requests
            break
        await asyncio.sleep(0.1)  # Small delay to not overwhelm the test runner

    # Assert
    assert response.status_code == 429
    assert "Too many requests" in response.text
