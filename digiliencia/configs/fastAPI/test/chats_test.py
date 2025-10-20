import uuid
import pytest
from httpx import AsyncClient
from starlette import status
from schemas.chat import TemplateList, ModelList

pytestmark = pytest.mark.asyncio


async def test_get_conversations_empty(authenticated_client: AsyncClient):
    """Tests that a new user has no conversations."""
    response = await authenticated_client.get("/conversations")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"conversations": []}


async def test_invalid_chat_operations(
    api_client: AsyncClient, authenticated_client: AsyncClient, templates: TemplateList
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
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    invalid_chat_data = {
        "tittle": "",  # Empty title
        "ia_prompt": "b0081876-19de-4e00-b1e5-824b39de290e",  # Invalid prompt
    }
    response = await authenticated_client.patch("/chats", json=invalid_chat_data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    invalid_chat_data = {}  # Missing required fields
    response = await authenticated_client.patch("/chats", json=invalid_chat_data)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    # Test sending invalid message
    template = next(iter(templates.items()))[1]
    chat_response = await authenticated_client.patch(
        "/chats", json={"tittle": "Test Chat", "ia_prompt": template}
    )
    assert chat_response.status_code == status.HTTP_201_CREATED

    chat_id = chat_response.json()["idChat"]

    invalid_message = {"text": ""}  # Empty message
    response = await authenticated_client.patch(
        f"/chats/{chat_id}", json=invalid_message
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT

    invalid_message = {}  # Missing required field
    response = await authenticated_client.patch(
        f"/chats/{chat_id}", json=invalid_message
    )
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT


async def test_get_nonexistent_chat(authenticated_client: AsyncClient):
    """Tests retrieving a chat that doesn't exist."""
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.get(f"/chats/{random_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_delete_nonexistent_chat(authenticated_client: AsyncClient):
    """Tests deleting a chat that doesn't exist."""
    random_uuid = str(uuid.uuid4())
    response = await authenticated_client.delete(f"/chats/{random_uuid}")
    assert response.status_code == status.HTTP_404_NOT_FOUND


async def test_chat_creation_and_messages(
    authenticated_client: AsyncClient, templates: TemplateList, models: ModelList
):
    """Tests creating a chat and sending/receiving messages."""
    # Getting templates

    template = next(iter(templates.items()))[1]
    model = next(iter(models.items()))[1]

    # Create new chat
    chat_data = {"tittle": "Test Chat", "ia_prompt": template}
    chat_response = await authenticated_client.patch("/chats", json=chat_data)
    assert chat_response.status_code == status.HTTP_201_CREATED
    chat_id = chat_response.json()["idChat"]

    # Add first message
    question1 = {"text": "What is FastAPI?", "model_id": model}
    response1 = await authenticated_client.patch(f"/chats/{chat_id}", json=question1)
    assert response1.status_code == status.HTTP_200_OK
    assert "text" in response1.json()

    # Add second message
    question2 = {"text": "How do I handle authentication?", "model_id": model}
    response2 = await authenticated_client.patch(f"/chats/{chat_id}", json=question2)
    assert response2.status_code == status.HTTP_200_OK
    assert "text" in response2.json()

    # Get conversation history
    chat_response = await authenticated_client.get(f"/chats/{chat_id}")
    assert chat_response.status_code == status.HTTP_200_OK
    messages = chat_response.json()

    # Verify message history
    assert len(messages) == 4  # 2 questions + 2 AI responses
    assert messages["messages"][0]["content"] == "What is FastAPI?"
    assert messages["messages"][2]["content"] == "How do I handle authentication?"
    # Verify AI responses exist
    assert messages["messages"][1]["content"]  # First AI response
    assert messages["messages"][3]["content"]  # Second AI response


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
        "/register", json={"email": other_email, "password": other_password}
    )
    assert register_response.status_code == status.HTTP_201_CREATED

    # Autenticar al segundo usuario
    login_response = await api_client.post(
        "/auth/login", json={"email": other_email, "password": other_password}
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
        "/register", json={"email": other_email, "password": other_password}
    )
    assert register_response.status_code == status.HTTP_201_CREATED

    # Autenticar al segundo usuario
    login_response = await api_client.post(
        "/auth/login", json={"email": other_email, "password": other_password}
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
