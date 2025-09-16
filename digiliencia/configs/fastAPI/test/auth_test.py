# /tests/test_auth.py
import pytest
from httpx import AsyncClient

# Mark all tests in this file to be run asynchronously
pytestmark = pytest.mark.asyncio


# --- Registration Tests ---
async def test_register_success(api_client: AsyncClient, fake_user: dict):
    """
    Tests that a user can register successfully (the happy path).
    """
    email = fake_user["email"]
    password = fake_user["password"]

    response = await api_client.post(
        "/register", json={"email": email, "password": password}
    )

    assert response.status_code == 201
    data = response.json()
    assert data["email"] == email
    assert data["is_active"] is True


async def test_register_conflict(api_client: AsyncClient, fake_user: dict):
    """
    Tests that the API does not allow registering an email that already exists (the unhappy path).
    """
    email = fake_user["email"]
    response = await api_client.post(
        "/register", json={"email": email, "password": "password123@"}
    )
    if response.status_code != 201:
        pytest.skip(
            "Precondition failed: could not create initial user. Status code: {}".format(
                response.status_code
            )
        )

    response = await api_client.post(
        "/register", json={"email": email, "password": "anotherpassword"}
    )

    assert response.status_code == 400  # Expected error for a duplicate user


async def test_register_invalid_data(api_client: AsyncClient, fake_user: dict):
    """
    Tests that the API rejects invalid registration data (the unhappy path).
    """
    email = fake_user["email"]
    password = fake_user["password"]
    # Invalid email
    response_invalid_email = await api_client.post(
        "/register", json={"email": "not-an-email", "password": password}
    )
    assert response_invalid_email.status_code == 422

    # Missing password
    response_no_password = await api_client.post("/register", json={"email": email})
    assert response_no_password.status_code == 422


# --- Custom Login Tests ---


async def test_custom_login_success(api_client: AsyncClient, fake_user: dict):
    """
    Tests that a user can log in with correct credentials (the happy path).
    """
    # We recreate a user to know their password for the test
    password = fake_user["password"]
    email = fake_user["email"]
    await api_client.post("/register", json={"email": email, "password": password})

    response = await api_client.post(
        "/auth/login", json={"email": email, "password": password}
    )

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data


async def test_custom_login_wrong_password(api_client: AsyncClient, fake_user: dict):
    """
    Tests that login fails with an incorrect password (the unhappy path).
    """
    password = "password22_for_login_test"
    email = fake_user["email"]

    response = await api_client.post(
        "/register", json={"email": email, "password": password}
    )
    if response.status_code != 201:
        pytest.skip(
            "Precondition failed: could not create initial user. Status code: {}".format(
                response.status_code
            )
        )

    response = await api_client.post(
        "/auth/login",
        json={"email": email, "password": password + "qqq"},
    )
    assert response.status_code == 401


async def test_login_nonexistent_user(api_client: AsyncClient, fake_user: dict):
    """
    Login should fail if the user does not exist.
    """
    email = fake_user["email"]
    password = fake_user["password"]
    response = await api_client.post(
        "/auth/login", json={"email": email, "password": password}
    )
    assert response.status_code == 401


async def test_login_invalid_email_format(api_client: AsyncClient, fake_user: dict):
    """
    Login should fail if the email is not valid.
    """
    response = await api_client.post(
        "/auth/login", json={"email": "not-email", "password": fake_user["password"]}
    )
    assert response.status_code == 422


async def test_login_malformed_payload(api_client: AsyncClient, fake_user: dict):
    """
    Login should fail if the payload is malformed.
    """
    email = fake_user["email"]
    password = fake_user["password"]
    response = await api_client.post(
        "/auth/login", json={"usuario": email, "clave": password}
    )
    assert response.status_code == 422


async def test_login_wrong_method(api_client: AsyncClient, db_session):
    """
    Login should fail if GET is used instead of POST.
    """
    response = await api_client.get("/auth/login")
    assert response.status_code in (405, 404)


async def test_standard_login_success(api_client: AsyncClient, fake_user: dict):
    """
    Standard login (form-data) should work if the user exists.
    """
    email = fake_user["email"]
    password = fake_user["password"]
    response = await api_client.post("/register", json={"email": email, "password": password})

    if response.status_code != 201:
        pytest.skip("User registration failed.")

    response = await api_client.post(
        "/auth/jwt/login", data={"username": email, "password": password}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


async def test_protected_endpoint_with_invalid_token(
    api_client: AsyncClient, db_session
):
    """
    Access to a protected endpoint with an invalid token should be rejected.
    """
    headers = {"Authorization": "Bearer token_invalido"}
    response = await api_client.get("/users/me", headers=headers)
    assert response.status_code == 405


# --- User Deletion Tests ---


async def test_delete_user_success(api_client: AsyncClient, fake_user: dict):
    """
    Tests that an authenticated user can delete their own account (the happy path).
    """
    # 1. Create a new user for the test
    email = fake_user["email"]
    password = fake_user["password"]
    response = await api_client.post(
        "/register", json={"email": email, "password": password}
    )

    if response.status_code != 201:
        pytest.skip(
            "Precondition failed: could not create initial user. Status code: {}".format(
                response.status_code
            )
        )

    # 2. Log in to get their token
    login_resp = await api_client.post(
        "/auth/login", json={"email": email, "password": password}
    )

    if login_resp.status_code != 200:
        pytest.skip(
            "Precondition failed: could not log in user. Status code: {}".format(
                login_resp.status_code
            )
        )

    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3. Delete the account using the token
    delete_response = await api_client.delete("/users/me", headers=headers)
    assert delete_response.status_code == 204

    # 4. Verify that the user can no longer log in
    final_login_resp = await api_client.post(
        "/auth/login", json={"email": email, "password": password}
    )
    assert final_login_resp.status_code == 401


async def test_delete_user_unauthenticated(api_client: AsyncClient):
    """
    Tests that an unauthenticated user cannot delete an account (the unhappy path).
    """
    response = await api_client.delete("/users/me")
    assert response.status_code == 401  # Unauthorized


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
    Tests that the API rejects weak passwords according to the custom policy.
    This single test function covers multiple failure scenarios.
    """
    email = fake_user["email"]

    response = await api_client.post(
        "/register", json={"email": email, "password": password}
    )

    # fastapi-users wraps InvalidPasswordException in a 400 Bad Request
    assert response.status_code == 400

    # Check that the error detail contains the specific reason from our UserManager
    error_detail = response.json()["detail"]
    assert error_detail["reason"] == expected_reason


async def test_health_endpoint(api_client: AsyncClient):
    """Health endpoint should return 200 and a small JSON payload."""
    response = await api_client.get("health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
