# /tests/health_test.py
import pytest
from starlette import status
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


# --- Health Check ---


@pytest.mark.asyncio
async def test_health_endpoint(api_client: AsyncClient):
    """
    Tests that the health check endpoint is available and returns the
    correct status message.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.

    Asserts:
        - The API returns a 200 OK status.
        - The response body matches the expected status JSON.
    """
    response = await api_client.get("/health")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok"}
