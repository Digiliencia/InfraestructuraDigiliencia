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


async def test_create_and_get_conversation(
    authenticated_client: AsyncClient, db_session
):
    """Test creating a conversation and immediately retrieving it."""
    # Crear un chat manualmente en la base de datos
    from db.models import Chat

    user_id = uuid.UUID(authenticated_client.headers["Authorization"].split()[1])
    chat = Chat(titulo="Test Chat", user_id=user_id)
    db_session.add(chat)
    await db_session.commit()
    await db_session.refresh(chat)

    # Obtener conversaciones
    response = await authenticated_client.get("/conversations")
    assert response.status_code == 200
    data = response.json()
    assert any(c["Título"] == "Test Chat" for c in data["conversations"].values())


async def test_patch_and_get_full_conversation(
    authenticated_client: AsyncClient, db_session
):
    """Test patching a conversation and retrieving its full content."""
    from db.models import Chat

    user_id = uuid.UUID(authenticated_client.headers["Authorization"].split()[1])
    chat = Chat(titulo="Conversación Patch", user_id=user_id)
    db_session.add(chat)
    await db_session.commit()
    await db_session.refresh(chat)

    # Preguntar al chat
    payload = {"model": "test-model", "text": "¿Cuál es la capital de Francia?"}
    response = await authenticated_client.patch(f"/chats/{chat.id}", json=payload)
    assert response.status_code == 200
    assert "Respuesta simulada" in response.json()["text"]

    # Obtener la conversación completa
    response = await authenticated_client.get(f"/chats/{chat.id}")
    assert response.status_code == 200
    texts = response.json()
    assert any("Francia" in t["text"] for t in texts)


async def test_put_and_delete_conversation(
    authenticated_client: AsyncClient, db_session
):
    """Test importing messages to a conversation, deleting the conversation, and ensuring it no longer exists."""
    from db.models import Chat

    user_id = uuid.UUID(authenticated_client.headers["Authorization"].split()[1])
    chat = Chat(titulo="Import Chat", user_id=user_id)
    db_session.add(chat)
    await db_session.commit()
    await db_session.refresh(chat)

    # Importar mensajes
    payload = [{"text": "Hola"}, {"text": "¿Qué tal?"}]
    response = await authenticated_client.put(f"/chats/{chat.id}", json=payload)
    assert response.status_code == 200
    assert len(response.json()) == 2

    # Borrar conversación
    response = await authenticated_client.delete(f"/chats/{chat.id}")
    assert response.status_code == 204

    # Comprobar que ya no existe
    response = await authenticated_client.get(f"/chats/{chat.id}")
    assert response.status_code == 404
