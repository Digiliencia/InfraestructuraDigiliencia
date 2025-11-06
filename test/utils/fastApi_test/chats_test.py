# /tests/test_chats.py
"""
This module contains integration tests for the chat-related API endpoints.

It covers the complete lifecycle of chat conversations, including creation,
retrieval of summaries and full histories, message passing, deletion, and
import functionality. It also includes critical tests for authorization,
ensuring users cannot access or modify chats belonging to others, and
verifies handling of various error conditions and invalid inputs.

Dependencies:
    - pytest: For running the tests and managing fixtures.
    - pytest-asyncio: For handling asynchronous test functions.
    - httpx: For making asynchronous HTTP requests to the test server.
"""

import uuid
import pytest
from httpx import AsyncClient
from starlette import status
from digiliencia.configs.fastAPI.schemas.chat import TemplateList, ModelList
import asyncio

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
    Tests that a newly registered user has no conversations.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client fixture.

    Asserts:
        - The API returns a 202 ACCEPTED status.
        - The response body is an empty list of conversations.
    """
    response = await authenticated_client.get(CONVERSATIONS)
    assert response.status_code == status.HTTP_202_ACCEPTED
    assert response.json() == {"conversations": []}


async def test_invalid_chat_operations(
    api_client: AsyncClient, authenticated_client: AsyncClient, templates: TemplateList
):
    """
    Tests various invalid operations and error cases for chat endpoints.

    This test covers multiple failure scenarios, including:
    - Unauthenticated access to protected endpoints.
    - Chat creation with invalid or nonexistent data.
    - Sending an invalid message to an existing chat.

    Args:
        api_client (AsyncClient): An unauthenticated HTTP client.
        authenticated_client (AsyncClient): An authenticated HTTP client.
        templates (TemplateList): A fixture providing a list of available AI prompts.

    Asserts:
        - Unauthenticated requests fail with 401 Unauthorized.
        - Requests with invalid data fail with 422 Unprocessable Content.
        - Requests with a valid but nonexistent prompt UUID fail with 400 Bad Request.
    """
    # Test unauthenticated access
    response = await api_client.get(CONVERSATIONS)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = await api_client.get(f"{CHATS_PATH}/1")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # Test invalid chat creation data (invalid UUID format)
    invalid_chat_data = {
        "tittle": "Test",
        "ia_prompt": "not-a-uuid",
    }
    response = await authenticated_client.patch(CHATS_PATH, json=invalid_chat_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # Test invalid chat creation data (nonexistent prompt UUID)
    invalid_chat_data = {
        "tittle": "Test",
        "ia_prompt": str(uuid.uuid4()),
    }
    response = await authenticated_client.patch(CHATS_PATH, json=invalid_chat_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    # Test missing required fields
    invalid_chat_data = {}
    response = await authenticated_client.patch(CHATS_PATH, json=invalid_chat_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # Test sending invalid message
    template_id = templates[0]["idTemplate"]
    chat_response = await authenticated_client.patch(
        CHATS_PATH, json={"tittle": "Test Chat", "ia_prompt": template_id}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["idChat"]

    invalid_message = {"text": ""}
    response = await authenticated_client.patch(
        f"{CHATS_PATH}/{chat_id}", json=invalid_message
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


async def test_get_nonexistent_chat(authenticated_client: AsyncClient):
    """
    Tests that retrieving a chat that does not exist fails correctly.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client.

    Asserts:
        - The API returns a 404 Not Found status.
    """
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.get(f"{CHATS_PATH}/{random_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_delete_nonexistent_chat(authenticated_client: AsyncClient):
    """
    Tests that deleting a chat that does not exist fails correctly.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client.

    Asserts:
        - The API returns a 404 Not Found status.
    """
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.delete(f"{CHATS_PATH}/{random_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_chat_creation_and_messages(
    authenticated_client: AsyncClient, templates: TemplateList, models: ModelList
):
    """
    Tests the full "happy path" lifecycle: creating a chat, sending multiple
    messages, and retrieving the complete conversation history.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client.
        templates (TemplateList): A fixture providing available AI prompts.
        models (ModelList): A fixture providing available AI models.

    Asserts:
        - The chat is created successfully (201 Created).
        - Messages are sent and received successfully (202 Accepted).
        - The retrieved conversation history contains the correct number of
          messages and the original user content.
    """
    template_id = templates[0]["idTemplate"]
    model_id = models[0]["idModel"]

    # Create new chat
    chat_data = {"tittle": "Test Chat", "template": template_id}
    chat_response = await authenticated_client.patch(CHATS_PATH, json=chat_data)
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["idChat"]

    # Add first message
    question1 = {"text": "What is FastAPI?", "model_id": model_id}
    response1 = await authenticated_client.patch(
        f"{CHATS_PATH}/{chat_id}", json=question1
    )
    assert response1.status_code == status.HTTP_202_ACCEPTED
    assert "text" in response1.json()

    # Add second message
    question2 = {"text": "How do I handle authentication?", "model_id": model_id}
    response2 = await authenticated_client.patch(
        f"{CHATS_PATH}/{chat_id}", json=question2
    )
    assert response2.status_code == status.HTTP_202_ACCEPTED
    assert "text" in response2.json()

    # Get conversation history
    chat_response = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    assert chat_response.status_code == status.HTTP_202_ACCEPTED
    conversation = chat_response.json()

    # Verify message history
    assert len(conversation["messages"]) == 4  # 2 questions + 2 AI responses
    assert conversation["messages"][0]["content"] == "What is FastAPI?"
    assert conversation["messages"][2]["content"] == "How do I handle authentication?"
    assert conversation["messages"][1]["content"]
    assert conversation["messages"][3]["content"]


async def test_get_other_user_chat(
    authenticated_client: AsyncClient,
    api_client: AsyncClient,
    fake_user: dict,
    templates: TemplateList,
):
    """
    Tests that a user cannot retrieve a chat belonging to another user.

    This is a critical authorization test that manually creates a second user,
    has them create a chat, and then verifies that the first user receives a
    404 Not Found error when trying to access it.

    Args:
        authenticated_client (AsyncClient): Client for the primary test user.
        api_client (AsyncClient): Unauthenticated client used to register and
                                  log in as the second user.
        fake_user (dict): A fixture to generate user credentials.
        templates (TemplateList): A fixture providing available AI prompts.

    Asserts:
        - User 1's request to get User 2's chat fails with 404 Not Found.
        - User 2 can still access their own chat successfully.
    """
    # Create and authenticate a second user
    other_email = "other_" + fake_user["email"]
    other_password = fake_user["password"]

    reg_resp = await api_client.post(
        REGISTER, json={"email": other_email, "password": other_password}
    )
    assert reg_resp.status_code == status.HTTP_201_CREATED

    login_resp = await api_client.post(
        LOGIN, json={"email": other_email, "password": other_password}
    )
    assert login_resp.status_code == status.HTTP_200_OK

    token = login_resp.json()["access_token"]
    api_client.headers.update({"Authorization": f"Bearer {token}"})

    # User 2 creates a chat
    template_id = templates[0]["idTemplate"]
    chat_data = {"tittle": "Other User's Chat", "ia_prompt": template_id}
    chat_response = await api_client.patch(CHATS_PATH, json=chat_data)
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["idChat"]

    # User 1 tries to access User 2's chat
    response = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Verify User 2 can still access their own chat
    chat_response = await api_client.get(f"{CHATS_PATH}/{chat_id}")
    assert chat_response.status_code == status.HTTP_202_ACCEPTED

    # Cleanup User 2
    await api_client.delete(USERS_ME)


async def test_import_conversation(
    authenticated_client: AsyncClient, templates: TemplateList
):
    """
    Tests creating a new chat by importing a conversation payload.

    This test verifies that the PUT /chats endpoint correctly creates a new
    chat with a new UUID based on the provided title, prompt, and messages.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client.
        templates (TemplateList): A fixture providing available AI prompts.

    Asserts:
        - The API returns a 202 Accpeted status with a summary of the new chat.
        - The summary does not contain the full message list.
        - A subsequent GET request to the new chat's ID retrieves the full,
          correctly imported conversation.
    """
    valid_ia_prompt_id = templates[0]["idTemplate"]

    import_payload = {
        "template": valid_ia_prompt_id,
        "tittle": "Imported Title",
        "texts": [{"text": "Imported Message 1"}, {"text": "Imported Message 2"}],
    }

    response = await authenticated_client.put(CHATS_PATH, json=import_payload)

    # Assert that the response is a summary of the new chat
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()

    assert "idChat" in response_data
    assert response_data["tittle"] == "Imported Title"
    assert response_data["template"] == valid_ia_prompt_id
    assert "messages" not in response_data

    new_chat_id = response_data["idChat"]

    # Verify that the full conversation was created correctly
    chat_response = await authenticated_client.get(f"{CHATS_PATH}/{new_chat_id}")

    assert chat_response.status_code == status.HTTP_202_ACCEPTED
    conversation = chat_response.json()

    assert conversation["tittle"] == "Imported Title"
    assert len(conversation["messages"]) == 2
    assert conversation["messages"][0]["content"] == "Imported Message 1"
    assert conversation["messages"][1]["content"] == "Imported Message 2"


async def test_delete_conversation(
    authenticated_client: AsyncClient, templates: TemplateList
):
    """
    Tests successful deletion of a conversation.

    This test creates a chat, deletes it, and then verifies that it can no
    longer be accessed and does not appear in the user's conversation list.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client.
        templates (TemplateList): A fixture providing available AI prompts.

    Asserts:
        - The delete request returns a 204 No Content status.
        - A subsequent GET request for the deleted chat fails with 404 Not Found.
        - The deleted chat's ID is not present in the user's conversation list.
    """
    template_id = templates[0]["idTemplate"]
    chat_response = await authenticated_client.patch(
        CHATS_PATH, json={"tittle": "Test Chat", "ia_prompt": template_id}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["idChat"]

    await authenticated_client.patch(
        f"{CHATS_PATH}/{chat_id}", json={"text": "Test message"}
    )

    # Delete the chat
    response = await authenticated_client.delete(f"{CHATS_PATH}/{chat_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verify chat was deleted
    chat_response = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    assert chat_response.status_code == status.HTTP_404_NOT_FOUND

    # Verify chat doesn't appear in conversations list
    convs_response = await authenticated_client.get(CONVERSATIONS)
    assert chat_id not in str(convs_response.json())


async def test_delete_other_user_chat(
    authenticated_client: AsyncClient,
    api_client: AsyncClient,
    fake_user: dict,
    templates: TemplateList,
    models: ModelList,
):
    """
    Tests that a user cannot delete a chat belonging to another user.

    This authorization test follows the same pattern as test_get_other_user_chat,
    verifying that a delete request from one user on another's resource fails.

    Args:
        authenticated_client (AsyncClient): Client for the primary test user.
        api_client (AsyncClient): Client used to act as the second user.
        fake_user (dict): A fixture to generate user credentials.
        templates (TemplateList): A fixture providing available AI prompts.

    Asserts:
        - User 1's request to delete User 2's chat fails with 404 Not Found.
        - User 2's chat still exists and is accessible to them.
        - The chat's content remains unchanged after the failed deletion attempt.
    """
    model_id = models[0]["idModel"]
    # Create and authenticate a second user
    other_email = "other_" + fake_user["email"]
    other_password = fake_user["password"]

    register_response = await api_client.post(
        REGISTER, json={"email": other_email, "password": other_password}
    )
    assert register_response.status_code == status.HTTP_201_CREATED

    login_response = await api_client.post(
        LOGIN, json={"email": other_email, "password": other_password}
    )
    assert login_response.status_code == status.HTTP_200_OK
    other_token = login_response.json()["access_token"]
    api_client.headers["Authorization"] = f"Bearer {other_token}"

    # User 2 creates a chat and adds a message
    template_id = templates[0]["idTemplate"]
    chat_response = await api_client.patch(
        CHATS_PATH, json={"tittle": "Other User's Chat", "ia_prompt": template_id}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["idChat"]

    # Add a test message to verify content preservation
    test_message = {"text": "Test Message", "model_id": model_id}
    message_response = await api_client.patch(
        f"{CHATS_PATH}/{chat_id}", json=test_message
    )
    assert message_response.status_code == status.HTTP_202_ACCEPTED

    # Get initial state of the chat
    initial_chat = await api_client.get(f"{CHATS_PATH}/{chat_id}")
    assert initial_chat.status_code == status.HTTP_202_ACCEPTED
    initial_content = initial_chat.json()

    # User 1 tries to delete the chat
    response = await authenticated_client.delete(f"{CHATS_PATH}/{chat_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Verify chat still exists for User 2 with unchanged content
    chat_response = await api_client.get(f"{CHATS_PATH}/{chat_id}")
    assert chat_response.status_code == status.HTTP_202_ACCEPTED
    final_content = chat_response.json()
    assert final_content == initial_content  # Verify no changes occurred

    # Verify User 2 can still modify their chat
    new_message = {"text": "Another message", "model_id": model_id}
    message_response = await api_client.patch(
        f"{CHATS_PATH}/{chat_id}", json=new_message
    )
    assert message_response.status_code == status.HTTP_202_ACCEPTED

    # Cleanup User 2
    await api_client.delete("/users/me")


async def test_chat_message_order_preservation(
    authenticated_client: AsyncClient, templates: TemplateList, models: ModelList
):
    """
    Tests that messages in a chat maintain their correct order and are not affected
    by concurrent operations.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client.
        templates (TemplateList): A fixture providing available AI prompts.
        models (ModelList): A fixture providing available AI models.

    Asserts:
        - Messages are stored in the correct order.
        - Message order is preserved after updates.
        - Each message maintains its original content.
    """
    # Create a new chat
    template_id = templates[0]["idTemplate"]
    chat_data = {"tittle": "Order Test Chat", "ia_prompt": template_id}
    chat_response = await authenticated_client.patch(CHATS_PATH, json=chat_data)
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["idChat"]

    # Send multiple messages in sequence
    model_id = models[0]["idModel"]
    messages = ["First message", "Second message", "Third message"]

    for msg in messages:
        response = await authenticated_client.patch(
            f"{CHATS_PATH}/{chat_id}", json={"text": msg, "model_id": model_id}
        )
        assert response.status_code == status.HTTP_202_ACCEPTED

    # Verify the chat history
    chat_response = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    assert chat_response.status_code == status.HTTP_202_ACCEPTED
    chat_data = chat_response.json()

    # Verify message order and content
    user_messages = [
        msg["content"] for msg in chat_data["messages"][::2]
    ]  # Every other message is user message
    assert user_messages == messages

    # Verify each message has unique order_number
    order_numbers = [msg["order_number"] for msg in chat_data["messages"]]
    assert len(order_numbers) == len(set(order_numbers))  # No duplicate order numbers
    assert order_numbers == sorted(order_numbers)  # Numbers are in ascending order


async def test_chat_concurrent_access(
    authenticated_client: AsyncClient, templates: TemplateList, models: ModelList
):
    """
    Tests that the chat endpoint lock prevents concurrent message processing.

    It sends multiple requests simultaneously to the same chat and asserts
    that only ONE request succeeds (202 Accepeted) and all others are rejected
    with a 409 Conflict.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client.
        templates (TemplateList): A fixture providing available AI prompts.
        models (ModelList): A fixture providing available AI models.

    Asserts:
        - Exactly one request returns HTTP_202_ACCEPTED.
        - All other requests return HTTP_409_CONFLICT.
        - The chat history contains exactly two messages (one user, one AI)
          from the single successful request.
    """
    template_id = templates[0]["idTemplate"]
    chat_data = {"tittle": "Concurrent Lock Test", "ia_prompt": template_id}
    chat_response = await authenticated_client.patch(CHATS_PATH, json=chat_data)
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["idChat"]

    model_id = models[0]["idModel"]
    num_requests = 5
    concurrent_messages = [
        {"text": f"Concurrent message {i}", "model_id": model_id}
        for i in range(num_requests)
    ]
    original_texts = {msg["text"] for msg in concurrent_messages}

    # asyncio.gather runs all request at the "same time",
    responses = await asyncio.gather(
        *[
            authenticated_client.patch(f"{CHATS_PATH}/{chat_id}", json=msg)
            for msg in concurrent_messages
        ]
    )

    status_codes = [response.status_code for response in responses]

    assert status_codes.count(status.HTTP_202_ACCEPTED) == 1
    assert status_codes.count(status.HTTP_409_CONFLICT) == num_requests - 1

    chat_response = await authenticated_client.get(f"{CHATS_PATH}/{chat_id}")
    assert chat_response.status_code == status.HTTP_202_ACCEPTED
    chat_data = chat_response.json()

    assert len(chat_data["messages"]) == 2

    user_msg = chat_data["messages"][0]
    ai_msg = chat_data["messages"][1]

    assert user_msg["order_number"] == 1
    assert user_msg["content"] in original_texts

    assert ai_msg["order_number"] == 2

    expected_ai_response = (
        f"Simulated response to '{user_msg['content']}' using model {model_id}"
    )
    assert ai_msg["content"] == expected_ai_response


async def test_chat_data_integrity(
    authenticated_client: AsyncClient, templates: TemplateList, models: ModelList
):
    """
    Tests the data integrity of chat operations, ensuring no unintended
    side effects occur during various operations.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client.
        templates (TemplateList): A fixture providing available AI prompts.
        models (ModelList): A fixture providing available AI models.

    Asserts:
        - Chat properties remain unchanged unless explicitly modified.
        - Deleting one chat doesn't affect others.
        - Message content is preserved exactly as sent.
    """
    # Create two chats
    template_id = templates[0]["idTemplate"]
    model_id = models[0]["idModel"]

    chat1_data = {"tittle": "First Chat", "ia_prompt": template_id}
    chat2_data = {"tittle": "Second Chat", "ia_prompt": template_id}

    chat1_response = await authenticated_client.patch(CHATS_PATH, json=chat1_data)
    assert chat1_response.status_code == status.HTTP_201_CREATED
    chat1_id = chat1_response.json()["idChat"]

    chat2_response = await authenticated_client.patch(CHATS_PATH, json=chat2_data)
    assert chat2_response.status_code == status.HTTP_201_CREATED
    chat2_id = chat2_response.json()["idChat"]

    # Add messages to both chats
    message1 = {"text": "Message in first chat", "model_id": model_id}
    message2 = {"text": "Message in second chat", "model_id": model_id}

    await authenticated_client.patch(f"{CHATS_PATH}/{chat1_id}", json=message1)
    await authenticated_client.patch(f"{CHATS_PATH}/{chat2_id}", json=message2)

    # Get initial state
    chat2_initial = await authenticated_client.get(f"{CHATS_PATH}/{chat2_id}")

    # Delete first chat
    response = await authenticated_client.delete(f"{CHATS_PATH}/{chat1_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verify second chat remains unchanged
    chat2_after = await authenticated_client.get(f"{CHATS_PATH}/{chat2_id}")
    assert chat2_after.status_code == status.HTTP_202_ACCEPTED
    assert chat2_after.json() == chat2_initial.json()

    # Verify first chat is really gone
    response = await authenticated_client.get(f"{CHATS_PATH}/{chat1_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Verify user's chat list is accurate
    conversations = await authenticated_client.get(CONVERSATIONS)
    assert conversations.status_code == status.HTTP_202_ACCEPTED
    conv_data = conversations.json()["conversations"]
    assert len(conv_data) == 1
    assert conv_data[0]["idChat"] == chat2_id


async def test_ask_question_to_nonexistent_chat(
    authenticated_client: AsyncClient, models: ModelList
):
    """
    Tests that sending a message to a nonexistent chat fails correctly.

    Args:
        authenticated_client (AsyncClient): An authenticated HTTP client.
        models (ModelList): A fixture providing available AI models.

    Asserts:
        - The API returns a 404 Not Found status.
        - The error doesn't affect other system operations.
    """
    random_uuid = str(uuid.uuid4())
    model_id = models[0]["idModel"]

    # Get initial conversations list
    initial_conversations = await authenticated_client.get(CONVERSATIONS)
    assert initial_conversations.status_code == status.HTTP_202_ACCEPTED
    initial_count = len(initial_conversations.json()["conversations"])

    # Try to send message to nonexistent chat
    question = {"text": "What is FastAPI?", "model_id": model_id}
    response = await authenticated_client.patch(
        f"{CHATS_PATH}/{random_uuid}", json=question
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Verify conversations list remained unchanged
    final_conversations = await authenticated_client.get(CONVERSATIONS)
    assert final_conversations.status_code == status.HTTP_202_ACCEPTED
    assert len(final_conversations.json()["conversations"]) == initial_count
