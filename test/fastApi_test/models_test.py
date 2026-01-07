# test/fastApi_test/models_test.py
"""
Integration tests for AI Models API GET by ID endpoint.

Covers:
- Retrieving a specific model by ID.
- Error handling (404 for non-existent models).
- Invalid UUID format handling.
"""

import uuid

import pytest
from httpx import AsyncClient
from starlette import status

from digiliencia.configs.fastAPI.core.endpoints import MODEL_LIST

pytestmark = pytest.mark.asyncio


async def test_get_model_by_id(api_client: AsyncClient):
    """
    Verify retrieving a specific model by ID.
    First get the list to extract a valid ID, then fetch that model.
    Status: 200 OK.
    """
    # Get list of models to find a valid ID
    list_response = await api_client.get(MODEL_LIST)
    assert list_response.status_code == status.HTTP_200_OK

    models = list_response.json()["models"]
    if not models:
        pytest.skip("No models available in database")

    # Get first model's ID
    model_id = models[0]["id"]

    # Fetch the specific model by ID
    response = await api_client.get(f"{MODEL_LIST}/{model_id}")
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert "id" in data
    assert "name" in data
    assert data["id"] == model_id
    assert isinstance(data["name"], str)


async def test_get_model_not_found(api_client: AsyncClient):
    """
    Verify 404 error when requesting a non-existent model.
    Status: 404 Not Found.
    """
    fake_id = str(uuid.uuid4())
    response = await api_client.get(f"{MODEL_LIST}/{fake_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    data = response.json()
    assert "detail" in data
    assert "not found" in data["detail"].lower()


async def test_get_model_invalid_id_format(api_client: AsyncClient):
    """
    Verify error handling for invalid UUID format.
    Status: 422 Unprocessable Entity.
    """
    invalid_id = "not-a-valid-uuid"
    response = await api_client.get(f"{MODEL_LIST}/{invalid_id}")

    # FastAPI will return 422 for invalid UUID format
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
