# tests/health_test.py
"""
Integration tests for the Health Check endpoint.

This endpoint is critical for container orchestration (Docker/Kubernetes)
and load balancers to verify the service is up and running.
"""

import pytest
from httpx import AsyncClient
from starlette import status

# Import centralized endpoint constant
from digiliencia.configs.fastAPI.core.endpoints import HEALTH_PATH

# Apply asyncio marker to all tests in this module
pytestmark = pytest.mark.asyncio


async def test_health_endpoint(api_client: AsyncClient):
    """
    Tests that the health check endpoint is available and returns the
    correct status message and service identifier.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.

    Asserts:
        - The API returns a 200 OK status.
        - The response body matches the expected structure defined in main.py.
    """
    response = await api_client.get(HEALTH_PATH)

    assert response.status_code == status.HTTP_200_OK

    # return {"status": "ok", "service": "fastapi-service"}
    expected_response = {"status": "ok", "service": "fastapi-service"}

    assert response.json() == expected_response
