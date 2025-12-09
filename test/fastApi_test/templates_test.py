# test/fastApi_test/templates_test.py
"""
Integration tests for AI Prompt Templates API GET by ID endpoint.

Covers:
- Retrieving a specific template by ID.
- Error handling (404 for non-existent templates).
- Invalid UUID format handling.
"""

import uuid

import pytest
from httpx import AsyncClient
from starlette import status

from digiliencia.configs.fastAPI.core.endpoints import TEMPLATE_LIST

pytestmark = pytest.mark.asyncio


async def test_get_template_by_id(api_client: AsyncClient):
    """
    Verify retrieving a specific template by ID.
    First get the list to extract a valid ID, then fetch that template.
    Status: 200 OK.
    """
    # Get list of templates to find a valid ID
    list_response = await api_client.get(TEMPLATE_LIST)
    assert list_response.status_code == status.HTTP_200_OK

    templates = list_response.json()["templates"]
    if not templates:
        pytest.skip("No templates available in database")

    # Get first template's ID
    template_id = templates[0]["id"]

    # Fetch the specific template by ID
    response = await api_client.get(f"{TEMPLATE_LIST}/{template_id}")
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "description" in data
    assert data["id"] == template_id
    assert isinstance(data["name"], str)
    assert isinstance(data["description"], str)


async def test_get_template_not_found(api_client: AsyncClient):
    """
    Verify 404 error when requesting a non-existent template.
    Status: 404 Not Found.
    """
    fake_id = str(uuid.uuid4())
    response = await api_client.get(f"{TEMPLATE_LIST}/{fake_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()


async def test_get_template_invalid_id_format(api_client: AsyncClient):
    """
    Verify error handling for invalid UUID format.
    Status: 422 Unprocessable Entity.
    """
    invalid_id = "not-a-valid-uuid"
    response = await api_client.get(f"{TEMPLATE_LIST}/{invalid_id}")

    # FastAPI will return 422 for invalid UUID format
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
