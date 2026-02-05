# /tests/test_middleware.py
"""
Integration tests for Application Middleware.

This module verifies the correct application of global middleware layers,
specifically focusing on Security Headers and CORS policies.
"""

import pytest
from httpx import AsyncClient
from starlette import status

from digiliencia.fastAPI.core.config import settings
from digiliencia.fastAPI.core.endpoints import HEALTH_PATH

pytestmark = pytest.mark.asyncio


async def test_security_headers_are_present(api_client: AsyncClient):
    """
    Verify that essential security headers are injected into responses.

    Checks for:
    - HSTS (Strict-Transport-Security)
    - No-Sniff (X-Content-Type-Options)
    - Clickjacking Protection (X-Frame-Options)
    - CSP (Content-Security-Policy)

    Args:
        api_client (AsyncClient): The unauthenticated test client.
    """
    # We use the Health endpoint as it's public and lightweight
    response = await api_client.get(HEALTH_PATH)

    assert response.status_code == status.HTTP_200_OK

    # 1. HSTS: Ensures browsers only use HTTPS
    assert "strict-transport-security" in response.headers
    assert "max-age=31536000" in response.headers["strict-transport-security"]

    # 2. Content Type Options: Prevents MIME-sniffing
    assert "x-content-type-options" in response.headers
    assert response.headers["x-content-type-options"] == "nosniff"

    # 3. Frame Options: Prevents Clickjacking (iframe embedding)
    assert "x-frame-options" in response.headers
    assert response.headers["x-frame-options"] == "DENY"

    # 4. CSP: Controls resources the user agent is allowed to load
    assert "content-security-policy" in response.headers


async def test_cors_headers_are_present(api_client: AsyncClient):
    """
    Verify that CORS headers are correctly returned for allowed origins.

    Simulates a browser request from an allowed origin defined in settings
    and checks if the server accepts it.

    Args:
        api_client (AsyncClient): The unauthenticated test client.
    """

    if not settings.ALLOWED_ORIGINS:
        pytest.skip("No ALLOWED_ORIGINS configured in settings to test CORS.")

    target_origin = settings.ALLOWED_ORIGINS[0]
    headers = {"Origin": target_origin}

    # Make a request simulating a cross-origin call
    response = await api_client.get(HEALTH_PATH, headers=headers)

    assert response.status_code == status.HTTP_200_OK

    # Assert that the server explicitly allows this origin
    assert "access-control-allow-origin" in response.headers
    assert response.headers["access-control-allow-origin"] == target_origin
