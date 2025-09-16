# /tests/test_chats.py
import pytest
import uuid
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_get_conversations_empty(authenticated_client: AsyncClient):
    """Tests that a new user has no conversations."""
    response = await authenticated_client.get("/conversations")
    assert response.status_code == 200
    assert response.json()["conversations"] == {}


async def test_get_unauthenticated(api_client: AsyncClient):
    """Cybersecurity Test: Ensure unauthenticated users cannot access chat endpoints."""
    response = await api_client.get("/conversations")
    assert response.status_code == 401

    response = await api_client.get("/chats/1")
    assert response.status_code == 401
