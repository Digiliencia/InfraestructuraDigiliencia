# tests/test_auth.py
"""
Integration tests for Authentication & User Management.

Tests cover:
- Registration (Success, Conflict, Validation)
- Login (JSON Custom, Form Standard, Invalid Credentials)
- Account Deletion
- Password Policy Enforcement
"""

import pytest
from httpx import AsyncClient
from starlette import status

# Use centralized endpoint definitions
from digiliencia.configs.fastAPI.core.endpoints import REGISTER, LOGIN, USERS_ME, TOKEN

pytestmark = pytest.mark.asyncio


# =============================================================================
# Registration Tests
# =============================================================================


async def test_register_success(api_client: AsyncClient, fake_user: dict):
    """
    Verify successful user registration returns 201 Created and correct data.
    """
    response = await api_client.post(REGISTER, json=fake_user)

    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert data["email"] == fake_user["email"]
    assert data["is_active"] is True


async def test_register_conflict(api_client: AsyncClient, fake_user: dict):
    """
    Verify duplicate email registration returns 400 Bad Request.
    """
    # 1. First registration
    response_1 = await api_client.post(REGISTER, json=fake_user)
    assert response_1.status_code == status.HTTP_201_CREATED

    # 2. Second registration (Duplicate)
    response_2 = await api_client.post(REGISTER, json=fake_user)
    assert response_2.status_code == status.HTTP_400_BAD_REQUEST


async def test_register_invalid_data(api_client: AsyncClient):
    """
    Verify 422 Unprocessable Entity for invalid email format or missing fields.
    """
    # Invalid email format
    response_invalid = await api_client.post(
        REGISTER, json={"email": "not-an-email", "password": "ValidPassword123!"}
    )
    assert response_invalid.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # Missing password field
    response_missing = await api_client.post(
        REGISTER, json={"email": "test@example.com"}
    )
    assert response_missing.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


# =============================================================================
# Login Tests (Custom JSON Endpoint)
# =============================================================================


async def test_custom_login_success(api_client: AsyncClient, fake_user: dict):
    """
    Verify successful JSON login returns 200 OK and a Bearer token.
    """
    # Register first
    await api_client.post(REGISTER, json=fake_user)

    # Login
    response = await api_client.post(LOGIN, json=fake_user)

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


async def test_custom_login_wrong_password(api_client: AsyncClient, fake_user: dict):
    """
    Verify login with incorrect password returns 401 Unauthorized.
    """
    await api_client.post(REGISTER, json=fake_user)

    response = await api_client.post(
        LOGIN,
        json={"email": fake_user["email"], "password": "WrongPassword123!"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


async def test_login_nonexistent_user(api_client: AsyncClient, fake_user: dict):
    """
    Verify login for non-existent user returns 401 Unauthorized.
    """
    response = await api_client.post(LOGIN, json=fake_user)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# =============================================================================
# Login Tests (Standard Form Endpoint)
# =============================================================================


async def test_standard_login_success(api_client: AsyncClient, fake_user: dict):
    """
    Verify standard form-data login works correctly (used by Swagger UI).
    """
    await api_client.post(REGISTER, json=fake_user)

    # Note: Standard FastAPI Users endpoint expects form-encoded data
    response = await api_client.post(
        TOKEN,
        data={"username": fake_user["email"], "password": fake_user["password"]},
    )
    assert response.status_code == status.HTTP_200_OK
    assert "access_token" in response.json()


async def test_protected_endpoint_with_invalid_token(api_client: AsyncClient):
    """
    Verify accessing protected route with bad token returns 401.
    """
    headers = {"Authorization": "Bearer invalid_token_string"}
    response = await api_client.delete(USERS_ME, headers=headers)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# =============================================================================
# User Deletion Tests
# =============================================================================


async def test_delete_user_success(api_client: AsyncClient, fake_user: dict):
    """
    Verify full lifecycle: Register -> Login -> Delete -> Fail Login.
    """
    # 1. Register
    await api_client.post(REGISTER, json=fake_user)

    # 2. Login
    login_resp = await api_client.post(LOGIN, json=fake_user)
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Delete Account
    delete_response = await api_client.delete(USERS_ME, headers=headers)
    assert delete_response.status_code == status.HTTP_204_NO_CONTENT

    # 4. Verify Login Fails
    final_login_resp = await api_client.post(LOGIN, json=fake_user)
    # Expect 401 (or 400 depending on implementation, usually 400 for "bad credentials")
    # But since user is gone, 400 is common for "invalid user/pass".
    # FastAPI Users typically returns 400 for bad login request content or 401/400 for failure.
    # Let's check for failure status generally or specific 400/401.
    assert final_login_resp.status_code in (
        status.HTTP_400_BAD_REQUEST,
        status.HTTP_401_UNAUTHORIZED,
    )


async def test_delete_user_unauthenticated(api_client: AsyncClient):
    """
    Verify deleting without auth returns 401.
    """
    response = await api_client.delete(USERS_ME)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


# =============================================================================
# Password Policy Tests
# =============================================================================


@pytest.mark.parametrize(
    "password, expected_status, partial_msg",
    [
        # Caso 1: Contraseña corta (< 8). Pydantic Schema lo detecta primero -> 422
        (
            "short",
            status.HTTP_422_UNPROCESSABLE_CONTENT,
            "String should have at least 8 characters",
        ),
        # Caso 2: Sin número. UserManager lo detecta -> 400
        (
            "longpassword",
            status.HTTP_400_BAD_REQUEST,
            "Password must contain at least one number",
        ),
        # Caso 3: Sin letra. UserManager lo detecta -> 400
        (
            "123456789",
            status.HTTP_400_BAD_REQUEST,
            "Password must contain at least one letter",
        ),
    ],
)
async def test_register_weak_password(
    api_client: AsyncClient, password, expected_status, partial_msg, fake_user: dict
):
    response = await api_client.post(
        REGISTER, json={"email": fake_user["email"], "password": password}
    )

    assert response.status_code == expected_status

    # Verificación opcional del mensaje de error
    if expected_status == status.HTTP_400_BAD_REQUEST:
        # Error de lógica de negocio (UserManager)
        assert partial_msg in str(response.json())
    elif expected_status == status.HTTP_422_UNPROCESSABLE_CONTENT:
        # Error de validación de Pydantic (Schema)
        # Buscamos 'password' en la ubicación del error
        assert "password" in str(response.json())
