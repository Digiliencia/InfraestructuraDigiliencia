import uuid
import pytest
from httpx import AsyncClient
from starlette import status

pytestmark = pytest.mark.asyncio


async def test_get_conversations_empty(authenticated_client: AsyncClient):
    """Tests that a new user has no conversations."""
    response = await authenticated_client.get("/conversations")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"conversations": []}


async def test_invalid_chat_operations(
    api_client: AsyncClient, authenticated_client: AsyncClient
):
    """Tests various invalid operations and error cases for chat endpoints."""
    # Test unauthenticated access
    response = await api_client.get("/conversations")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    response = await api_client.get("/chats/1")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # Test invalid chat creation data
    invalid_chat_data = {
        "tittle": "",  # Empty title
        "ia_prompt": "dfdsfdsgfh",  # Invalid prompt
    }
    response = await authenticated_client.patch("/chats", json=invalid_chat_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    invalid_chat_data = {}  # Missing required fields
    response = await authenticated_client.patch("/chats", json=invalid_chat_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Test sending invalid message
    response = await authenticated_client.get("/chats/template_list")
    if response.status_code != status.HTTP_202_ACCEPTED:
        raise Exception("Error getting templates. ", response.status_code)
    template = response.json()[0]
    chat_response = await authenticated_client.patch(
        "/chats", json={"tittle": "Test Chat", "ia_prompt": next(iter(template))}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    invalid_message = {"text": ""}  # Empty message
    response = await authenticated_client.patch(
        f"/chats/{chat_id}", json=invalid_message
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    invalid_message = {}  # Missing required field
    response = await authenticated_client.patch(
        f"/chats/{chat_id}", json=invalid_message
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


async def test_get_nonexistent_chat(authenticated_client: AsyncClient):
    """Tests retrieving a chat that doesn't exist."""
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.get(f"/chats/{random_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_chat_creation_and_messages(authenticated_client: AsyncClient):
    """Tests creating a chat and sending/receiving messages."""
    # Create new chat
    chat_data = {"tittle": "Test Chat", "ia_prompt": "You are a helpful assistant"}
    chat_response = await authenticated_client.post("/chats", json=chat_data)
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # Add first message
    question1 = {"text": "What is FastAPI?", "model": "test-model"}
    response1 = await authenticated_client.patch(f"/chats/{chat_id}", json=question1)
    assert response1.status_code == status.HTTP_200_OK
    assert "text" in response1.json()

    # Add second message
    question2 = {"text": "How do I handle authentication?", "model": "test-model"}
    response2 = await authenticated_client.patch(f"/chats/{chat_id}", json=question2)
    assert response2.status_code == status.HTTP_200_OK
    assert "text" in response2.json()

    # Get conversation history
    response = await authenticated_client.get(f"/chats/{chat_id}")
    assert response.status_code == status.HTTP_200_OK
    messages = response.json()

    # Verify message history
    assert len(messages) == 4  # 2 questions + 2 AI responses
    assert messages[0]["text"] == "What is FastAPI?"
    assert messages[2]["text"] == "How do I handle authentication?"
    # Verify AI responses exist
    assert messages[1]["text"]  # First AI response
    assert messages[3]["text"]  # Second AI response


async def test_create_and_list_chats(authenticated_client: AsyncClient):
    """Tests creating new chats and listing them."""
    # Create first chat
    chat1_data = {"tittle": "Test Chat 1", "ia_prompt": "You are a helpful assistant"}
    chat1_response = await authenticated_client.post("/chats", json=chat1_data)
    assert chat1_response.status_code == status.HTTP_201_CREATED
    #chat1_id = chat1_response.json()["id"]

    # Create second chat
    chat2_data = {"tittle": "Test Chat 2", "ia_prompt": "You are a technical expert"}
    chat2_response = await authenticated_client.post("/chats", json=chat2_data)
    assert chat2_response.status_code == status.HTTP_201_CREATED
    #chat2_id = chat2_response.json()["id"]

    # Get conversations list
    response = await authenticated_client.get("/conversations")
    assert response.status_code == status.HTTP_200_OK
    conversations = response.json()["conversations"]

    # Verify response structure and data
    assert len(conversations) == 2
    chat_tittles = [conv["tittle"] for conv in conversations]
    assert "Test Chat 1" in chat_tittles
    assert "Test Chat 2" in chat_tittles

    # Verify chat details
    for conv in conversations:
        assert "idChat" in conv
        assert "tittle" in conv
        assert "ia_prompt" in conv
        if conv["tittle"] == "Test Chat 1":
            assert conv["ia_prompt"] == "You are a helpful assistant"
        else:
            assert conv["ia_prompt"] == "You are a technical expert"


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
    assert register_response.status_code == status.HTTP_201_CREATED

    # Autenticar al segundo usuario
    login_response = await api_client.post(
        "/auth/login", data={"username": other_email, "password": other_password}
    )
    assert login_response.status_code == status.HTTP_200_OK
    other_token = login_response.json()["access_token"]

    # Crear un cliente autenticado para el segundo usuario
    api_client.headers["Authorization"] = f"Bearer {other_token}"

    # Crear un chat con el segundo usuario
    chat_response = await api_client.post(
        "/chats", json={"tittle": "Other User's Chat"}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # Try to access with first user
    response = await authenticated_client.get(f"/chats/{chat_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Verify chat exists for the second user
    chat_response = await api_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == status.HTTP_200_OK


async def test_ask_question_to_chat(authenticated_client: AsyncClient):
    """Tests asking a question to a chat and verifying the response."""
    # Create test chat with custom prompt
    chat_data = {
        "tittle": "Technical Support Chat",
        "ia_prompt": "You are a technical support assistant",
    }
    chat_response = await authenticated_client.post("/chats", json=chat_data)
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # Ask a technical question
    question = {"model": "test-model", "text": "How do I debug a Python application?"}
    response = await authenticated_client.patch(f"/chats/{chat_id}", json=question)
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert "text" in response_data
    assert isinstance(response_data["text"], str)
    assert len(response_data["text"]) > 0

    # Verify messages in chat history
    chat_response = await authenticated_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == status.HTTP_200_OK
    messages = chat_response.json()
    assert len(messages) == 2  # Question and AI response
    assert messages[0]["text"] == "How do I debug a Python application?"
    assert len(messages[1]["text"]) > 0  # AI response should not be empty

    # Verify message structure
    for message in messages:
        assert "text" in message
        assert isinstance(message["text"], str)
        assert "timestamp" in message


async def test_import_conversation(authenticated_client: AsyncClient):
    """Tests importing a conversation."""
    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # Add initial message through API
    initial_question = {"model": "test-model", "text": "Initial message"}
    await authenticated_client.patch(f"/chats/{chat_id}", json=initial_question)

    # Import new conversation
    new_messages = [{"text": "Message 1"}, {"text": "Message 2"}]
    response = await authenticated_client.put(f"/chats/{chat_id}", json=new_messages)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 2
    assert response.json()[0]["text"] == "Message 1"
    assert response.json()[1]["text"] == "Message 2"

    # Verify old messages were replaced
    chat_response = await authenticated_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == status.HTTP_200_OK
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
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # Add a message
    question = {"model": "test-model", "text": "Test message"}
    await authenticated_client.patch(f"/chats/{chat_id}", json=question)

    # Delete the chat
    response = await authenticated_client.delete(f"/chats/{chat_id}")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # Verify chat was deleted
    chat_response = await authenticated_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == status.HTTP_404_NOT_FOUND

    # Verify chat doesn't appear in conversations list
    convs_response = await authenticated_client.get("/chats/conversations")
    assert chat_id not in str(convs_response.json())


async def test_delete_nonexistent_chat(authenticated_client: AsyncClient):
    """Tests deleting a chat that doesn't exist."""
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.delete(f"/chats/{random_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


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
    assert register_response.status_code == status.HTTP_201_CREATED

    # Autenticar al segundo usuario
    login_response = await api_client.post(
        "/auth/login", data={"username": other_email, "password": other_password}
    )
    assert login_response.status_code == status.HTTP_200_OK
    other_token = login_response.json()["access_token"]

    # Crear un cliente autenticado para el segundo usuario
    api_client.headers["Authorization"] = f"Bearer {other_token}"

    # Crear un chat con el segundo usuario
    chat_response = await api_client.post(
        "/chats", json={"tittle": "Other User's Chat"}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # Intentar eliminar el chat con el primer usuario
    response = await authenticated_client.delete(f"/chats/{chat_id}")
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # Verificar que el chat sigue existiendo para el segundo usuario
    chat_response = await api_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == status.HTTP_200_OK


async def test_ask_question_to_nonexistent_chat(
    authenticated_client: AsyncClient,
):
    """Tests asking a question to a nonexistent chat."""
    random_uuid = str(uuid.uuid4())
    question = {"model": "test-model", "text": "Test question?"}
    response = await authenticated_client.patch(f"/chats/{random_uuid}", json=question)
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_ask_question_with_invalid_data(authenticated_client: AsyncClient):
    """Tests asking a question with invalid data."""
    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # Test missing required fields
    response = await authenticated_client.patch(
        f"/chats/{chat_id}",
        json={"text": "Test question?"},  # Missing model field
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    response = await authenticated_client.patch(
        f"/chats/{chat_id}",
        json={"model": "test-model"},  # Missing text field
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Test empty fields
    response = await authenticated_client.patch(
        f"/chats/{chat_id}", json={"model": "", "text": ""}
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


async def test_import_conversation_validation(authenticated_client: AsyncClient):
    """Tests validation when importing conversations."""
    # Create test chat
    chat_response = await authenticated_client.post(
        "/chats", json={"tittle": "Test Chat"}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["id"]

    # Test empty list
    response = await authenticated_client.put(f"/chats/{chat_id}", json=[])
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Test invalid message format
    response = await authenticated_client.put(
        f"/chats/{chat_id}",
        json=[{"wrong_field": "Message 1"}],  # Campo incorrecto
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # Test non-list payload
    response = await authenticated_client.put(
        f"/chats/{chat_id}",
        json={"text": "Single message"},  # Debería ser una lista
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
