# /tests/test_auth.py
import pytest
import uuid
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio

async def test_register_success(api_client: AsyncClient, db_session):
    """Tests a successful user registration."""
    email = f"test_{uuid.uuid4()}@example.com"
    password = "superPassword"
    
    response = await api_client.post("/register", json={"email": email, "password": password})
    
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == email
    assert data["is_active"] is True
    assert "id" in data
    
    # Cleanup
    user_in_db = await db_session.get(User, uuid.UUID(data["id"]))
    await db_session.delete(user_in_db)
    await db_session.commit()


async def test_register_conflict(api_client: AsyncClient, authenticated_client: AsyncClient):
    """Tests that a user cannot register with an already existing email."""
    # The authenticated client has already created a user. We get their email.
    user_info_resp = await authenticated_client.get("/users/me")
    email = user_info_resp.json()["email"]
    
    response = await api_client.post("/register", json={"email": email, "password": "anotherpassword"})
    
    assert response.status_code == 400 # fastapi-users returns 400 by default for duplicate users

async def test_login_success(api_client: AsyncClient, db_session):
    """Tests a successful login."""
    # Arrange: Create a user manually for the test
    email = f"login_{uuid.uuid4()}@example.com"
    password = "aVerySecurePassword123"
    register_payload = {"email": email, "password": password}
    register_response = await api_client.post("/register", json=register_payload)
    assert register_response.status_code == 201
    user_id = register_response.json()["id"]

    # Act: Log in
    login_payload = {"username": email, "password": password}
    response = await api_client.post("/auth/jwt/login", data=login_payload)
    
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    
    # Cleanup
    user_in_db = await db_session.get(User, uuid.UUID(user_id))
    await db_session.delete(user_in_db)
    await db_session.commit()

async def test_login_wrong_password(api_client: AsyncClient):
    """Tests that login fails with an incorrect password."""
    login_payload = {"username": "test@example.com", "password": "wrongpassword"}
    response = await api_client.post("/auth/jwt/login", data=login_payload)
    assert response.status_code == 400 # fastapi-users returns 400 for incorrect credentials

async def test_logout(authenticated_client: AsyncClient):
    """Tests that the logout endpoint works for an authenticated user."""
    response = await authenticated_client.post("/auth/jwt/logout")
    assert response.status_code == 200