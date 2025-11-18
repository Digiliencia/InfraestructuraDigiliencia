# /tests/test_auth.py
"""
This module contains integration tests for user authentication and management.

It covers the entire user lifecycle, including registration, login (both JSON
and form-based), token validation, account deletion, and enforcement of security
policies like password strength.

Dependencies:
    - pytest: For running the tests and managing fixtures.
    - pytest-asyncio: For handling asynchronous test functions.
    - httpx: For making asynchronous HTTP requests to the test server.
"""

import pytest
from httpx import AsyncClient
from starlette import status
from digiliencia.configs.fastAPI.core.endpoints import REGISTER, LOGIN, USERS_ME

pytestmark = pytest.mark.asyncio


# --- Registration Tests ---


async def test_register_success(api_client: AsyncClient, fake_user: dict):
    """
    Tests successful user registration.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.
        fake_user (dict): A fixture providing fake user credentials.

    Asserts:
        - The API returns a 201 Created status.
        - The response body contains the correct email and active status.
    """
    response = await api_client.post(REGISTER, json=fake_user)

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == fake_user["email"]
    assert data["is_active"] is True


async def test_register_conflict(api_client: AsyncClient, fake_user: dict):
    """
    Tests that registering an email that already exists fails.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.
        fake_user (dict): A fixture providing fake user credentials.

    Asserts:
        - The API returns a 400 Bad Request status on the second attempt.
    """
    response = await api_client.post(REGISTER, json=fake_user)
    if response.status_code != status.HTTP_201_CREATED:
        raise AssertionError(f"Precondition failed: {response.status_code}")

    # Try to register again
    response = await api_client.post(REGISTER, json=fake_user)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


async def test_register_invalid_data(api_client: AsyncClient):
    """
    Tests that registration fails with invalid data payloads.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.

    Asserts:
        - The API returns a 422 Unprocessable Content for an invalid email.
        - The API returns a 422 Unprocessable Content for a missing password.
    """
    # Invalid email
    response_invalid_email = await api_client.post(
        REGISTER, json={"email": "not-an-email", "password": "ValidPassword123"}
    )
    assert response_invalid_email.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # Missing password
    response_no_password = await api_client.post(
        REGISTER, json={"email": "test@example.com"}
    )
    assert response_no_password.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


# --- Custom (JSON) Login Tests ---


async def test_custom_login_success(api_client: AsyncClient, fake_user: dict):
    """
    Tests successful user login with a JSON payload.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.
        fake_user (dict): A fixture providing fake user credentials.

    Asserts:
        - The API returns a 202 Accepeted status.
        - The response body contains an 'access_token' and 'token_type'.
    """
    await api_client.post(REGISTER, json=fake_user)

    response = await api_client.post(LOGIN, json=fake_user)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


async def test_custom_login_wrong_password(api_client: AsyncClient, fake_user: dict):
    """
    Tests that login fails with an incorrect password.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.
        fake_user (dict): A fixture providing fake user credentials.

    Asserts:
        - The API returns a 401 Unauthorized status.
    """
    await api_client.post(REGISTER, json=fake_user)

    response = await api_client.post(
        LOGIN,
        json={"email": fake_user["email"], "password": "wrong-password"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_login_nonexistent_user(api_client: AsyncClient, fake_user: dict):
    """
    Tests that login fails if the user does not exist.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.
        fake_user (dict): A fixture providing fake user credentials for a user
                          that will not be registered.

    Asserts:
        - The API returns a 401 Unauthorized status.
    """
    response = await api_client.post(LOGIN, json=fake_user)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# --- Standard (Form) Login Tests ---


async def test_standard_login_success(api_client: AsyncClient, fake_user: dict):
    """
    Tests that the standard form-data login endpoint works correctly.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.
        fake_user (dict): A fixture providing fake user credentials.

    Asserts:
        - The API returns a 202 Accpeted status.
        - The response body contains an 'access_token'.
    """
    await api_client.post(REGISTER, json=fake_user)

    response = await api_client.post(
        "/auth/jwt/login",
        data={"username": fake_user["email"], "password": fake_user["password"]},
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()


async def test_protected_endpoint_with_invalid_token(api_client: AsyncClient):
    """
    Tests that a protected endpoint rejects requests with an invalid token.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.

    Asserts:
        - The API returns a 401 Unauthorized status.
    """
    headers = {"Authorization": "Bearer invalid_token"}
    response = await api_client.delete(USERS_ME, headers=headers)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# --- User Deletion Tests ---


async def test_delete_user_success(api_client: AsyncClient, fake_user: dict):
    """
    Tests the full lifecycle of user deletion: register, log in, delete,
    and verify inability to log in again.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.
        fake_user (dict): A fixture providing fake user credentials.

    Asserts:
        - The deletion request returns a 204 No Content status.
        - A subsequent login attempt for the deleted user fails with 401 Unauthorized.
    """
    # 1. Create user
    await api_client.post(REGISTER, json=fake_user)

    # 2. Log in
    login_resp = await api_client.post(LOGIN, json=fake_user)
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Delete account
    delete_response = await api_client.delete(USERS_ME, headers=headers)
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT

    # 4. Verify user can no longer log in
    final_login_resp = await api_client.post(LOGIN, json=fake_user)
    assert final_login_resp.status_code == status.HTTP_401_UNAUTHORIZED


async def test_delete_user_unauthenticated(api_client: AsyncClient):
    """
    Tests that an unauthenticated request to the delete user endpoint fails.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.

    Asserts:
        - The API returns a 401 Unauthorized status.
    """
    response = await api_client.delete(USERS_ME)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# --- Password Policy Tests ---


@pytest.mark.parametrize(
    "password, expected_reason",
    [
        ("short", "La contraseña debe tener al menos 8 caracteres."),
        ("longpassword", "La contraseña debe contener al menos un número."),
        ("123456789", "La contraseña debe contener al menos una letra."),
    ],
)
async def test_register_weak_password(
    api_client: AsyncClient, password, expected_reason, fake_user: dict
):
    """
    Tests that the API rejects weak passwords according to the defined policy.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.
        password (str): The weak password to test, provided by pytest.mark.parametrize.
        expected_reason (str): The expected error message from the API.
        fake_user (dict): A fixture providing a fake email.

    Asserts:
        - The API returns a 400 Bad Request status.
        - The response detail contains the specific reason for the failure.
    """
    response = await api_client.post(
        REGISTER, json={"email": fake_user["email"], "password": password}
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    error_detail = response.json()["detail"]
    assert error_detail["reason"] == expected_reason
