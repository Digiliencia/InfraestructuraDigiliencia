# /tests/test_auth.py
import pytest
import uuid
from httpx import AsyncClient

# Mark all tests in this file to be run asynchronously
pytestmark = pytest.mark.asyncio

# --- Registration Tests ---


async def test_register_success(api_client: AsyncClient, db_session):
    """
    Tests that a user can register successfully (the happy path).
    """
    email = f"test_{uuid.uuid4()}@example.com"
    password = "aVerySecurePassword123"

    response = await api_client.post(
        "/register", json={"email": email, "password": password}
    )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == email
    assert data["is_active"] is True


async def test_register_conflict(
    api_client: AsyncClient, authenticated_client: AsyncClient
):
    """
    Tests that the API does not allow registering an email that already exists (the unhappy path).
    """
    # authenticated_client fixture already creates a user. We get their email.
    user_info_resp = await authenticated_client.get("/users/me")
    email = user_info_resp.json()["email"]

    response = await api_client.post(
        "/register", json={"email": email, "password": "anotherpassword"}
    )

    assert response.status_code == 400  # Expected error for a duplicate user


async def test_register_invalid_data(api_client: AsyncClient):
    """
    Tests that the API rejects invalid registration data (the unhappy path).
    """
    # Invalid email
    response_invalid_email = await api_client.post(
        "/register", json={"email": "not-an-email", "password": "password123"}
    )
    assert response_invalid_email.status_code == 422

    # Missing password
    response_no_password = await api_client.post(
        "/register", json={"email": "test@example.com"}
    )
    assert response_no_password.status_code == 422


# --- Custom Login Tests ---


async def test_custom_login_success(
    api_client: AsyncClient, authenticated_client: AsyncClient
):
    """
    Tests that a user can log in with correct credentials (the happy path).
    """
    # We recreate a user to know their password for the test
    password = "password_for_login_test"
    email = "login-test@example.com"
    await api_client.post("/register", json={"email": email, "password": password})

    response = await api_client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


async def test_custom_login_wrong_password(api_client: AsyncClient):
    """
    Tests that login fails with an incorrect password (the unhappy path).
    """
    response = await api_client.post(
        "/api/auth/login",
        json={"email": "user@example.com", "password": "wrongpassword"},
    )
    assert response.status_code == 400


async def test_login_nonexistent_user(api_client: AsyncClient):
    """
    Login should fail if the user does not exist.
    """
    response = await api_client.post(
        "/auth/login", json={"email": "noexiste@example.com", "password": "irrelevante"}
    )
    assert response.status_code in (400, 401)


async def test_login_invalid_email_format(api_client: AsyncClient):
    """
    Login should fail if the email is not valid.
    """
    response = await api_client.post(
        "/auth/login", json={"email": "no-es-email", "password": "irrelevante"}
    )
    assert response.status_code == 422


async def test_login_malformed_payload(api_client: AsyncClient):
    """
    Login should fail if the payload is malformed.
    """
    response = await api_client.post(
        "/auth/login", json={"usuario": "test", "clave": "123"}
    )
    assert response.status_code == 422


async def test_login_wrong_method(api_client: AsyncClient):
    """
    Login should fail if GET is used instead of POST.
    """
    response = await api_client.get("/auth/login")
    assert response.status_code in (405, 404)


async def test_standard_login_success(api_client: AsyncClient):
    """
    Standard login (form-data) should work if the user exists.
    """
    email = f"std_login_{uuid.uuid4()}@example.com"
    password = "aVerySecurePassword123"
    await api_client.post("/register", json={"email": email, "password": password})
    response = await api_client.post(
        "/auth/jwt/login", data={"username": email, "password": password}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


async def test_protected_endpoint_with_invalid_token(api_client: AsyncClient):
    """
    Access to a protected endpoint with an invalid token should be rejected.
    """
    headers = {"Authorization": "Bearer token_invalido"}
    response = await api_client.get("/users/me", headers=headers)
    assert response.status_code == 401


# --- User Deletion Tests ---


async def test_delete_user_success(api_client: AsyncClient):
    """
    Tests that an authenticated user can delete their own account (the happy path).
    """
    # 1. Create a new user for the test
    email = f"to_delete_{uuid.uuid4()}@example.com"
    password = "aVerySecurePassword123"
    await api_client.post("/register", json={"email": email, "password": password})

    # 2. Log in to get their token
    login_resp = await api_client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Delete the account using the token
    delete_response = await api_client.delete("/api/users/me", headers=headers)
    assert delete_response.status_code == 204

    # 4. Verify that the user can no longer log in
    final_login_resp = await api_client.post(
        "/api/auth/login", json={"email": email, "password": password}
    )
    assert final_login_resp.status_code == 400


async def test_delete_user_unauthenticated(api_client: AsyncClient):
    """
    Tests that an unauthenticated user cannot delete an account (the unhappy path).
    """
    response = await api_client.delete("/api/users/me")
    assert response.status_code == 401  # Unauthorized


# --- Password Policy Tests ---


@pytest.mark.parametrize(
    "password, expected_reason",
    [
        ("short", "At least 8 characters."),
        ("longpassword", "At least one number."),
        ("123456789", "At least one character."),
    ],
)
async def test_register_weak_password(
    api_client: AsyncClient, password, expected_reason
):
    """
    Tests that the API rejects weak passwords according to the custom policy.
    This single test function covers multiple failure scenarios.
    """
    email = f"weak_pass_{uuid.uuid4()}@example.com"

    response = await api_client.post(
        "/register", json={"email": email, "password": password}
    )

    # fastapi-users wraps InvalidPasswordException in a 400 Bad Request
    assert response.status_code == 400

    # Check that the error detail contains the specific reason from our UserManager
    error_detail = response.json()["detail"]
    assert expected_reason in error_detail
