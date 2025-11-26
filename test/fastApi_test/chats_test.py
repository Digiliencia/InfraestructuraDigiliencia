# tests/test_chats.py
"""
Integration tests for Chat API endpoints.

Covers:
- Conversation lifecycle (Create, List, Get, Delete).
- Message interaction (Send, Receive).
- Authorization boundaries (User Isolation).
- Concurrent access control (Redis Lock).
- Data integrity and import flows.
"""

import asyncio
import uuid

import pytest
from httpx import AsyncClient
from starlette import status

# Import Schemas
from digiliencia.configs.fastAPI.schemas.chat import Templates, Models

# Import Centralized Endpoints
from digiliencia.configs.fastAPI.core.endpoints import (
    CONVERSATIONS,
    CHATS_PATH,
    REGISTER,
    LOGIN,
    USERS_ME,
)

pytestmark = pytest.mark.asyncio


async def test_get_conversations_empty(authenticated_client: AsyncClient):
    """
    Verify a new user has an empty conversation list.
    Status: 200 OK.
    """
    response = await authenticated_client.get(CONVERSATIONS)
    # Updated: GET now returns 200 OK
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"conversations": []}


async def test_invalid_chat_operations(
    api_client: AsyncClient, authenticated_client: AsyncClient, templates: Templates
):
    """
    Verify error handling for unauthorized access and invalid payloads.
    """
    # 1. Unauthenticated Access
    response = await api_client.get(CONVERSATIONS)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = await api_client.get(f"{CHATS_PATH}/{uuid.uuid4()}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # 2. Invalid UUID format
    # Updated field: 'ai_prompt_id' instead of 'ia_prompt'
    invalid_chat_data = {
        "title": "Test",
        "ai_prompt_id": "not-a-uuid",
    }
    response = await authenticated_client.patch(CHATS_PATH, json=invalid_chat_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # 3. Nonexistent Prompt UUID
    invalid_chat_data = {
        "title": "Test",
        "ai_prompt_id": str(uuid.uuid4()),
    }
    response = await authenticated_client.patch(CHATS_PATH, json=invalid_chat_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # 4. Missing Fields
    response = await authenticated_client.patch(CHATS_PATH, json={})
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # 5. Invalid Message Content (Empty)
    # Create valid chat first
    # Updated: Schema uses 'id' instead of 'idTemplate'
    template_id = templates.templates[0].id
    chat_response = await authenticated_client.patch(
        CHATS_PATH, json={"title": "Test Chat", "ai_prompt_id": str(template_id)}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    # Updated: 'id' instead of 'idChat'
    chat_id = chat_response.json()["id"]

    # Try sending empty content
    # Updated: 'content' instead of 'text'
    invalid_message = {"content": ""}
    response = await authenticated_client.patch(
        f"{CHATS_PATH}/{chat_id}", json=invalid_message
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


async def test_get_nonexistent_chat(authenticated_client: AsyncClient):
    """
    Verify accessing a random UUID returns 404.
    """
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.get(f"{CHATS_PATH}/{random_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_delete_nonexistent_chat(authenticated_client: AsyncClient):
    """
    Verify deleting a random UUID returns 404.
    """
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.delete(f"{CHATS_PATH}/{random_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_chat_creation_and_messages(
    authenticated_client: AsyncClient, templates: Templates, models: Models
):
    """
    Happy Path: Create Chat -> Send Messages -> Get History.
    """
    template_id = templates.templates[0].id
    model_id = models.models[0].id

    # 1. Create Chat
    chat_data = {"title": "Test Chat", "ai_prompt_id": str(template_id)}
    chat_response = await authenticated_client.patch(CHATS_PATH, json=chat_data)
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # 2. Send Message 1
    # Updated: 'content' instead of 'text'
    msg1 = {"content": "What is FastAPI?", "model_id": str(model_id)}
    response1 = await authenticated_client.patch(f"{CHATS_PATH}/{chat_id}", json=msg1)
    # Updated: Patch returns 200 OK with AI response
    assert response1.status_code == status.HTTP_200_OK
    assert "text" in response1.json()

    # 3. Send Message 2
    msg2 = {"content": "How do I handle auth?", "model_id": str(model_id)}
    response2 = await authenticated_client.patch(f"{CHATS_PATH}/{chat_id}", json=msg2)
    assert response2.status_code == status.HTTP_200_OK

    # 4. Get History
    history_response = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    assert history_response.status_code == status.HTTP_200_OK
    conversation = history_response.json()

    # Verify
    assert len(conversation["messages"]) == 4  # 2 User + 2 AI
    assert conversation["messages"][0]["content"] == "What is FastAPI?"
    assert conversation["messages"][2]["content"] == "How do I handle auth?"


async def test_get_other_user_chat(
    authenticated_client: AsyncClient,
    api_client: AsyncClient,
    fake_user: dict,
    templates: Templates,
):
    """
    Verify User Isolation: User A cannot see User B's chats.
    """
    # 1. Setup User B
    other_email = "other_" + fake_user["email"]
    other_pass = fake_user["password"]

    await api_client.post(REGISTER, json={"email": other_email, "password": other_pass})
    login_resp = await api_client.post(
        LOGIN, json={"email": other_email, "password": other_pass}
    )
    other_token = login_resp.json()["access_token"]

    # 2. User B creates a chat
    # Use a separate client instance or update headers temporarily
    # Here we update api_client headers manually
    api_client.headers.update({"Authorization": f"Bearer {other_token}"})

    template_id = templates.templates[0].id
    chat_data = {"title": "User B Chat", "ai_prompt_id": str(template_id)}
    chat_resp = await api_client.patch(CHATS_PATH, json=chat_data)
    chat_id = chat_resp.json()["id"]

    # 3. User A tries to access it
    response = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # 4. Cleanup User B
    await api_client.delete(USERS_ME)


async def test_import_conversation(
    authenticated_client: AsyncClient, templates: Templates
):
    """
    Verify creating a chat via import (bulk messages).
    """
    template_id = templates.templates[0].id

    # Updated payload keys: 'ai_prompt_id' and 'texts' structure
    import_payload = {
        "ai_prompt_id": str(template_id),
        "title": "Imported Chat",
        "texts": [{"text": "Msg 1"}, {"text": "Msg 2"}],
    }

    response = await authenticated_client.put(CHATS_PATH, json=import_payload)

    assert response.status_code == status.HTTP_201_CREATED
    summary = response.json()

    assert summary["title"] == "Imported Chat"
    assert summary["ai_prompt_id"] == str(template_id)

    # Verify content
    new_chat_id = summary["id"]
    full_chat = await authenticated_client.get(f"{CHATS_PATH}/{new_chat_id}")
    messages = full_chat.json()["messages"]

    assert len(messages) == 2
    assert messages[0]["content"] == "Msg 1"
    assert messages[1]["content"] == "Msg 2"


async def test_delete_conversation(
    authenticated_client: AsyncClient, templates: Templates
):
    """
    Verify deleting a chat removes it from the list.
    """
    template_id = templates.templates[0].id
    create_resp = await authenticated_client.patch(
        CHATS_PATH, json={"title": "To Delete", "ai_prompt_id": str(template_id)}
    )
    chat_id = create_resp.json()["id"]

    # Delete
    del_resp = await authenticated_client.delete(f"{CHATS_PATH}/{chat_id}")
    assert del_resp.status_code == status.HTTP_204_NO_CONTENT

    # Verify Gone
    get_resp = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    assert get_resp.status_code == status.HTTP_404_NOT_FOUND

    # Verify not in list
    list_resp = await authenticated_client.get(CONVERSATIONS)
    # Simple check if ID string is present in the JSON dump
    assert str(chat_id) not in str(list_resp.json())


async def test_chat_message_order_preservation(
    authenticated_client: AsyncClient, templates: Templates, models: Models
):
    """
    Verify messages are stored and retrieved in the correct sequence.
    """
    template_id = templates.templates[0].id
    model_id = models.models[0].id

    # Create Chat
    resp = await authenticated_client.patch(
        CHATS_PATH, json={"title": "Order Test", "ai_prompt_id": str(template_id)}
    )
    chat_id = resp.json()["id"]

    messages = ["First", "Second", "Third"]

    for msg in messages:
        await authenticated_client.patch(
            f"{CHATS_PATH}/{chat_id}", json={"content": msg, "model_id": str(model_id)}
        )

    # Get History
    history_resp = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    history = history_resp.json()

    # Filter User messages (every 2nd message is usually AI response)
    # Assuming the loop above generated 3 User + 3 AI = 6 messages
    all_msgs = history["messages"]

    # If your logic saves user message with passed model_id, this works.
    # Otherwise, check by index [0, 2, 4]
    user_content_by_index = [all_msgs[i]["content"] for i in range(0, 6, 2)]

    assert user_content_by_index == messages

    # Verify Order Numbers
    order_nums = [m["order_number"] for m in all_msgs]
    assert order_nums == sorted(order_nums)


async def test_chat_concurrent_access(
    authenticated_client: AsyncClient, templates: Templates, models: Models
):
    """
    Verify Redis Lock prevents race conditions.
    """
    template_id = templates.templates[0].id
    model_id = models.models[0].id

    # Create Chat
    resp = await authenticated_client.patch(
        CHATS_PATH, json={"title": "Lock Test", "ai_prompt_id": str(template_id)}
    )
    chat_id = resp.json()["id"]

    # Prepare concurrent requests
    num_reqs = 5
    payloads = [
        {"content": f"Msg {i}", "model_id": str(model_id)} for i in range(num_reqs)
    ]

    # Execute
    responses = await asyncio.gather(
        *[
            authenticated_client.patch(f"{CHATS_PATH}/{chat_id}", json=p)
            for p in payloads
        ]
    )

    status_codes = [r.status_code for r in responses]

    # Assertions
    # Only 1 should succeed (200 OK), others should fail (409 Conflict)
    assert status_codes.count(status.HTTP_200_OK) == 1
    assert status_codes.count(status.HTTP_409_CONFLICT) == num_reqs - 1

    # Verify only 2 messages (1 User + 1 AI) were added
    history = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    assert len(history.json()["messages"]) == 2


async def test_ask_question_to_nonexistent_chat(
    authenticated_client: AsyncClient, models: Models
):
    """
    Verify posting a message to a bad UUID returns 404.
    """
    random_id = str(uuid.uuid4())
    model_id = models.models[0].id

    payload = {"content": "Hello?", "model_id": str(model_id)}
    response = await authenticated_client.patch(
        f"{CHATS_PATH}/{random_id}", json=payload
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
