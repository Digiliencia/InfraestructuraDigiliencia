# /tests/test_middleware.py
import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


# Test to ensure security headers are added to responses.
async def test_security_headers_are_present(api_client: AsyncClient):
    """
    Cybersecurity Test: Verifies that essential security headers are present in the response.
    """
    # Arrange: Make a request to any endpoint
    response = await api_client.get("/")  # The root endpoint is fine for this

    # Assert: Check for the presence and content of key security headers
    assert response.status_code == 200
    assert "Strict-Transport-Security" in response.headers
    assert "X-Content-Type-Options" in response.headers
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert "X-Frame-Options" in response.headers
    assert response.headers["X-Frame-Options"] == "DENY"


# Test to ensure CORS headers are working correctly.
async def test_cors_headers_are_present(api_client: AsyncClient):
    """
    Tests that CORS middleware adds the correct headers for allowed origins.
    """
    # Arrange: Define an origin that is allowed in the API's configuration
    allowed_origin = "http://localhost:3000"
    headers = {"Origin": allowed_origin}

    # Act: Make a request with the Origin header
    response = await api_client.get("/", headers=headers)

    # Assert
    assert response.status_code == 200
    assert "access-control-allow-origin" in response.headers
    assert response.headers["access-control-allow-origin"] == allowed_origin
