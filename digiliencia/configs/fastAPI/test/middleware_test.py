# /tests/test_middleware.py
"""
This module contains integration tests for the FastAPI application's middleware.

It verifies the correct behavior of security-related middleware, including the
injection of essential security headers and the proper functioning of the
Cross-Origin Resource Sharing (CORS) policy.

Dependencies:
    - pytest: For running the tests and managing fixtures.
    - pytest-asyncio: For handling asynchronous test functions.
    - httpx: For making asynchronous HTTP requests to the test server.
"""

import pytest
from httpx import AsyncClient
from starlette import status

pytestmark = pytest.mark.asyncio


async def test_security_headers_are_present(api_client: AsyncClient):
    """
    Tests that essential security headers are present in standard API responses.

    This cybersecurity test verifies that the security middleware correctly
    injects headers designed to mitigate common web vulnerabilities like
    protocol downgrade attacks (HSTS), MIME-sniffing (X-Content-Type-Options),
    and clickjacking (X-Frame-Options).

    Args:
        api_client (AsyncClient): An asynchronous HTTP client fixture for making
                                  requests to the test server.

    Asserts:
        - The response status code is 200 OK.
        - The 'Strict-Transport-Security' header is present.
        - The 'X-Content-Type-Options' header is present and set to 'nosniff'.
        - The 'X-Frame-Options' header is present and set to 'DENY'.
    """
    # Arrange: No special arrangement is needed; a simple request is sufficient.
    # Act: Make a request to a root endpoint.
    response = await api_client.get("/")

    # Assert: Check for the presence and content of key security headers.
    assert response.status_code == status.HTTP_200_OK
    assert "Strict-Transport-Security" in response.headers
    assert "X-Content-Type-Options" in response.headers
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert "X-Frame-Options" in response.headers
    assert response.headers["X-Frame-Options"] == "DENY"


async def test_cors_headers_are_present(api_client: AsyncClient):
    """
    Tests that CORS and Content-Security-Policy headers are correctly applied.

    This test simulates a request from a browser at a specifically allowed
    origin. It verifies that the CORS middleware correctly responds with the
    'Access-Control-Allow-Origin' header, and that the security middleware
    also includes the 'Content-Security-Policy' header.

    Args:
        api_client (AsyncClient): An asynchronous HTTP client fixture for making
                                  requests to the test server.

    Asserts:
        - The response status code is 200 OK.
        - The 'Content-Security-Policy' header exists and has the correct value.
        - The 'Access-Control-Allow-Origin' header matches the requested origin.
    """
    # Arrange: Define an origin that should be allowed by the API's configuration.
    allowed_origin = "http://localhost:3000"
    headers = {"Origin": allowed_origin}

    # Act: Make a request with the specified 'Origin' header.
    response = await api_client.get("/", headers=headers)

    # Assert: Verify both security and CORS headers.
    assert response.status_code == status.HTTP_200_OK

    # Assert that the Content-Security-Policy header exists.
    assert "content-security-policy" in response.headers
    assert response.headers["content-security-policy"] == "default-src 'self'"

    # Assert that the CORS header correctly reflects the allowed origin.
    assert response.headers["access-control-allow-origin"] == allowed_origin
