# test/v2_chats_test.py
import pytest
import uuid
from httpx import AsyncClient
from starlette import status
from digiliencia.fastAPI.schemas.chat import Templates, Models

# Use relative paths (V1 style but with v2 prefix)
# Joining with base_url "http://.../api"
V2_CHATS_PREFIX = "v2/chats"
V2_CONVERSATIONS = f"{V2_CHATS_PREFIX}/conversations"

pytestmark = pytest.mark.asyncio

async def test_v2_get_conversations_empty(authenticated_client: AsyncClient):
    """Verify v2 empty conversation list."""
    response = await authenticated_client.get(V2_CONVERSATIONS)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"conversations": []}

async def test_v2_chat_creation_and_messages(
    authenticated_client: AsyncClient, templates: Templates, models: Models
):
    """Verify V2 Chat Lifecycle: Create -> Send -> History."""
    template_id = templates.templates[0].id
    model_id = models.models[0].id

    # 1. Create Chat V2
    chat_data = {"title": "V2 Test Chat", "ai_prompt_id": str(template_id)}
    # Use relative path without leading slash to avoid host-root resolution
    chat_response = await authenticated_client.patch(V2_CHATS_PREFIX, json=chat_data)
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # 2. Send Message V2
    msg = {"content": "Hello V2", "model_id": str(model_id)}
    response = await authenticated_client.patch(f"{V2_CHATS_PREFIX}/{chat_id}", json=msg)
    assert response.status_code == status.HTTP_200_OK
    assert "text" in response.json()

    # 3. Get History V2
    history_response = await authenticated_client.get(f"{V2_CHATS_PREFIX}/{chat_id}")
    assert history_response.status_code == status.HTTP_200_OK
    conversation = history_response.json()
    assert len(conversation["messages"]) == 2

async def test_v2_delete_conversation(
    authenticated_client: AsyncClient, templates: Templates
):
    """Verify deleting a chat via V2."""
    template_id = templates.templates[0].id
    
    # Create valid chat for deletion
    chat_data = {"title": "V2 Delete", "ai_prompt_id": str(template_id)}
    create_resp = await authenticated_client.patch(V2_CHATS_PREFIX, json=chat_data)
    assert create_resp.status_code == status.HTTP_201_CREATED
    chat_id = create_resp.json()["id"]

    # Delete V2
    del_resp = await authenticated_client.delete(f"{V2_CHATS_PREFIX}/{chat_id}")
    assert del_resp.status_code == status.HTTP_204_NO_CONTENT

    # Verify Gone
    get_resp = await authenticated_client.get(f"{V2_CHATS_PREFIX}/{chat_id}")
    assert get_resp.status_code == status.HTTP_404_NOT_FOUND
