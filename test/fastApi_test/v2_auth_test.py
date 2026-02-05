# test/v2_auth_test.py
import pytest
from httpx import AsyncClient
from starlette import status

# Relative paths (no leading slash)
V2_AUTH_PREFIX = "v2/auth"
V2_LOGIN = f"{V2_AUTH_PREFIX}/login"
V2_REGISTER = f"{V2_AUTH_PREFIX}/register"

pytestmark = pytest.mark.asyncio


async def test_v2_auth_lifecycle(api_client: AsyncClient, fake_user: dict):
    """Verify V2 Auth Lifecycle: Register -> Login."""
    # 1. Register V2
    reg_response = await api_client.post(V2_REGISTER, json=fake_user)
    assert reg_response.status_code == status.HTTP_201_CREATED

    # 2. Login V2
    login_response = await api_client.post(
        V2_LOGIN, json={"email": fake_user["email"], "password": fake_user["password"]}
    )
    assert login_response.status_code == status.HTTP_200_OK
    assert "access_token" in login_response.json()
