import uuid
import pytest
from httpx import AsyncClient

pytestmark = pytest.mark.asyncio


async def test_get_conversations_empty(authenticated_client: AsyncClient):
    """Tests that a new user has no conversations."""
    response = await authenticated_client.get("/conversations")
    assert response.status_code == 200
    assert response.json()["conversations"] == []


async def test_get_unauthenticated(api_client: AsyncClient):
    """Cybersecurity Test: Ensure unauthenticated users cannot access chat endpoints."""
    response = await api_client.get("/chats/conversations")
    assert response.status_code == 401

    response = await api_client.get("/chats/1")
    assert response.status_code == 401

async def test_get_nonexistent_chat(authenticated_client: AsyncClient):
    """Tests retrieving a chat that doesn't exist."""
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.get(f"/chats/{random_uuid}")
    assert response.status_code == 404

async def test_get_chat_messages(authenticated_client: AsyncClient):
    """Tests retrieving messages from a specific chat."""
    # Create test chat
    chat_response = await authenticated_client.patch("/chats")
    assert chat_response.status_code == 201
    chat_id = chat_response.json()["id"]

    # Add messages through the API
    question1 = {"model": "test-model", "text": "Message 1"}
    response1 = await authenticated_client.patch(f"/chats/{chat_id}", json=question1)
    assert response1.status_code == 200

    question2 = {"model": "test-model", "text": "Message 2"}
    response2 = await authenticated_client.patch(f"/chats/{chat_id}", json=question2)
    assert response2.status_code == 200

    # Get messages
    response = await authenticated_client.get(f"/chats/{chat_id}")
    assert response.status_code == 200
    messages = response.json()
    assert len(messages) == 4  # 2 preguntas + 2 respuestas
    assert messages[0]["text"] == "Message 1"
    assert messages[2]["text"] == "Message 2"


async def test_get_conversations_with_data(authenticated_client: AsyncClient):
    """Tests retrieving conversations when the user has existing chats."""
    # Create test chats using the API
    chat1_response = await authenticated_client.get(
        "/chats", json={"tittle": "Test Chat 1"}
    )
    assert chat1_response.status_code == 201

    chat2_response = await authenticated_client.get(
        "/chats", json={"tittle": "Test Chat 2"}
    )
    assert chat2_response.status_code == 201

    # Get conversations
    response = await authenticated_client.get("/conversations")
    assert response.status_code == 200
    conversations = response.json()["conversations"]
    assert len(conversations) == 2
    assert all(
        conv["Título"] in ["Test Chat 1", "Test Chat 2"]
        for conv in conversations.values()
    )

async def test_get_other_user_chat(
    authenticated_client: AsyncClient,
    api_client: AsyncClient,
    fake_user: dict,
):
    """Tests that users cannot access other users' chats."""
    # Crear un segundo usuario y autenticarlo
    other_email = "other_" + fake_user["email"]
    other_password = fake_user["password"] + "_other"

    # Registrar el segundo usuario
    register_response = await api_client.post(
        "/auth/register", json={"email": other_email, "password": other_password}
    )
    assert register_response.status_code == 201

    # Autenticar al segundo usuario
    login_response = await api_client.post(
        "/auth/login", data={"username": other_email, "password": other_password}
    )
    assert login_response.status_code == 200
    other_token = login_response.json()["access_token"]

    # Crear un cliente autenticado para el segundo usuario
    api_client.headers["Authorization"] = f"Bearer {other_token}"

    # Crear un chat con el segundo usuario
    chat_response = await api_client.post(
        "/chats", json={"tittle": "Other User's Chat"}
    )
    assert chat_response.status_code == 201
    chat_id = chat_response.json()["id"]

    # Try to access with first user
    response = await authenticated_client.get(f"/chats/{chat_id}")
    assert response.status_code == 404

    # Verify chat exists for the second user
    chat_response = await api_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == 200


async def test_ask_question_to_chat(authenticated_client: AsyncClient):
    """Tests asking a question to a chat."""
    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == 201
    chat_id = chat_response.json()["id"]

    # Ask a question
    question = {"model": "test-model", "text": "Test question?"}
    response = await authenticated_client.patch(f"/chats/{chat_id}", json=question)
    assert response.status_code == 200
    assert "text" in response.json()
    assert "Test question?" in response.json()["text"]

    # Verify messages in chat history
    chat_response = await authenticated_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == 200
    messages = chat_response.json()
    assert len(messages) == 2  # Question and answer
    assert messages[0]["text"] == "Test question?"
    assert "Test question?" in messages[1]["text"]


async def test_import_conversation(authenticated_client: AsyncClient):
    """Tests importing a conversation."""
    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == 201
    chat_id = chat_response.json()["id"]

    # Add initial message through API
    initial_question = {"model": "test-model", "text": "Initial message"}
    await authenticated_client.patch(f"/chats/{chat_id}", json=initial_question)

    # Import new conversation
    new_messages = [{"text": "Message 1"}, {"text": "Message 2"}]
    response = await authenticated_client.put(f"/chats/{chat_id}", json=new_messages)
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["text"] == "Message 1"
    assert response.json()[1]["text"] == "Message 2"

    # Verify old messages were replaced
    chat_response = await authenticated_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == 200
    messages = chat_response.json()
    assert len(messages) == 2
    assert messages[0]["text"] == "Message 1"
    assert messages[1]["text"] == "Message 2"


async def test_delete_conversation(authenticated_client: AsyncClient):
    """Tests deleting a conversation."""
    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == 201
    chat_id = chat_response.json()["id"]

    # Add a message
    question = {"model": "test-model", "text": "Test message"}
    await authenticated_client.patch(f"/chats/{chat_id}", json=question)

    # Delete the chat
    response = await authenticated_client.delete(f"/chats/{chat_id}")
    assert response.status_code == 204

    # Verify chat was deleted
    chat_response = await authenticated_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == 404

    # Verify chat doesn't appear in conversations list
    convs_response = await authenticated_client.get("/chats/conversations")
    assert chat_id not in str(convs_response.json())


async def test_delete_nonexistent_chat(authenticated_client: AsyncClient):
    """Tests deleting a chat that doesn't exist."""
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.delete(f"/chats/{random_uuid}")
    assert response.status_code == 404


async def test_delete_other_user_chat(
    authenticated_client: AsyncClient,
    api_client: AsyncClient,
    fake_user: dict,
):
    """Tests that users cannot delete other users' chats."""
    # Crear un segundo usuario y autenticarlo
    other_email = "other_" + fake_user["email"]
    other_password = fake_user["password"] + "_other"

    # Registrar el segundo usuario
    register_response = await api_client.post(
        "/auth/register", json={"email": other_email, "password": other_password}
    )
    assert register_response.status_code == 201

    # Autenticar al segundo usuario
    login_response = await api_client.post(
        "/auth/login", data={"username": other_email, "password": other_password}
    )
    assert login_response.status_code == 200
    other_token = login_response.json()["access_token"]

    # Crear un cliente autenticado para el segundo usuario
    api_client.headers["Authorization"] = f"Bearer {other_token}"

    # Crear un chat con el segundo usuario
    chat_response = await api_client.post(
        "/chats", json={"tittle": "Other User's Chat"}
    )
    assert chat_response.status_code == 201
    chat_id = chat_response.json()["id"]

    # Intentar eliminar el chat con el primer usuario
    response = await authenticated_client.delete(f"/chats/{chat_id}")
    assert response.status_code == 404

    # Verificar que el chat sigue existiendo para el segundo usuario
    chat_response = await api_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == 200


async def test_ask_question_to_nonexistent_chat(
    authenticated_client: AsyncClient,
):
    """Tests asking a question to a nonexistent chat."""
    random_uuid = str(uuid.uuid4())
    question = {"model": "test-model", "text": "Test question?"}
    response = await authenticated_client.patch(f"/chats/{random_uuid}", json=question)
    assert response.status_code == 404


async def test_ask_question_with_invalid_data(authenticated_client: AsyncClient):
    """Tests asking a question with invalid data."""
    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == 201
    chat_id = chat_response.json()["id"]

    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == 201
    chat_id = chat_response.json()["id"]

    # Test missing required fields
    response = await authenticated_client.patch(
        f"/chats/{chat_id}",
        json={"text": "Test question?"},  # Missing model field
    )
    assert response.status_code == 422

    response = await authenticated_client.patch(
        f"/chats/{chat_id}",
        json={"model": "test-model"},  # Missing text field
    )
    assert response.status_code == 422

    # Test empty fields
    response = await authenticated_client.patch(
        f"/chats/{chat_id}", json={"model": "", "text": ""}
    )
    assert response.status_code == 422


async def test_import_conversation_validation(authenticated_client: AsyncClient):
    """Tests validation when importing conversations."""
    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == 201
    chat_id = chat_response.json()["id"]

    # Test empty list
    response = await authenticated_client.put(f"/chats/{chat_id}", json=[])
    assert (
        response.status_code == 422
    )  # O el código que corresponda según la implementación

    # Test invalid message format
    response = await authenticated_client.put(
        f"/chats/{chat_id}",
        json=[{"wrong_field": "Message 1"}],  # Campo incorrecto
    )
    assert response.status_code == 422

    # Test non-list payload
    response = await authenticated_client.put(
        f"/chats/{chat_id}",
        json={"text": "Single message"},  # Debería ser una lista
    )
    assert response.status_code == 422
