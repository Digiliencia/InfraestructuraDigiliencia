# /api/routers/chats.py
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Model, User, Chat, Message
from schemas import chat as chat_schema
from auth.users import fastapi_users
from db.session import get_db

router = APIRouter()


@router.get(
    "/conversations",
    response_model=chat_schema.ConversationList,
    summary="List User Conversations",
    description="Retrieve a list of all conversations for the authenticated user",
    response_description="Dictionary of conversations with their IDs and titles",
    responses={
        200: {
            "description": "List of user's conversations",
            "content": {
                "application/json": {
                    "example": {
                        "conversations": {
                            "conversation1": {
                                "idChat": "550e8400-e29b-41d4-a716-446655440000",
                                "Título": "General Questions",
                            },
                            "conversation2": {
                                "idChat": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
                                "Título": "Technical Support",
                            },
                        }
                    }
                }
            },
        },
        401: {
            "description": "Not authenticated",
            "content": {
                "application/json": {"example": {"detail": "Not authenticated"}}
            },
        },
    },
)
async def get_user_conversations(
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    """
    Retrieve all conversations for the authenticated user.

    This endpoint returns a list of all chat conversations associated with the
    authenticated user, including their IDs and titles. The conversations are
    sorted by their creation date.

    Security:
    - Requires authentication
    - Users can only see their own conversations
    - Active account required

    Parameters:
        user (User): Current authenticated user (injected)
        db (AsyncSession): Database session (injected)

    Returns:
        ConversationList: Dictionary containing:
            - conversations (dict): Map of conversation IDs to their details
                - idChat (UUID): Unique identifier for the chat
                - Título (str): Title/name of the conversation

    Example:
        ```json
        {
            "conversations": {
                "conversation1": {
                    "idChat": "550e8400-e29b-41d4-a716-446655440000",
                    "Título": "General Questions"
                },
                "conversation2": {
                    "idChat": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
                    "Título": "Technical Support"
                }
            }
        }
        ```
    """
    result = await db.execute(select(Chat).where(Chat.user_id == user.id))
    chats = result.scalars().all()
    convs = {
        f"conversation{chat.id}": {"idChat": str(chat.id), "Título": chat.titulo}
        for chat in chats
    }
    return {"conversations": convs}


@router.get("/chats/{chat_id}", response_model=List[chat_schema.Texts])
async def get_full_conversation(
    chat_id: uuid.UUID,
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    """
    Retrieve a full conversation by its ID.

    Parameters:
        chat_id (UUID): The unique identifier of the chat
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        List[Texts]: List of messages in the conversation

    Raises:
        HTTPException: If chat is not found or user is not authorized
    """
    chat = await db.get(Chat, chat_id)
    if not chat or chat.user_id != user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    result = await db.execute(
        select(Message).where(Message.chat_id == chat_id).order_by(Message.n_orden)
    )
    messages = result.scalars().all()
    return [{"text": m.content} for m in messages]


@router.patch("/chats/{chat_id}", response_model=chat_schema.Texts)
async def ask_question_to_chat(
    chat_id: uuid.UUID,
    payload: chat_schema.Text,
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    """
    Send a question to a specific chat and get an AI-generated response.

    Parameters:
        chat_id (UUID): The unique identifier of the chat
        payload (Text): Contains the question text and model configuration
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        Texts: The AI-generated response

    Raises:contenido
        HTTPException: If chat is not found or user is not authorized
    """
    chat = await db.get(Chat, chat_id)
    if not chat or chat.user_id != user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    # Guardar la pregunta
    n_orden = (
        (await db.execute(select(Message.n_orden).where(Message.chat_id == chat_id)))
        .scalars()
        .all()
    )
    n_orden = max(n_orden) + 1 if n_orden else 1
    message = Message(chat_id=chat_id, order_number=n_orden, content=payload.text)
    db.add(message)
    await db.commit()
    await db.refresh(message)
    # Llamada a servicio externo (placeholder)
    respuesta = (
        f"Respuesta simulada a '{payload.text}' usando el modelo {payload.model}"
    )
    # Guardar la respuesta
    n_orden += 1
    response_message = Message(chat_id=chat_id, order_number=n_orden, content=respuesta)
    db.add(response_message)
    await db.commit()
    await db.refresh(response_message)
    return {"text": respuesta}

@router.patch("/chats/", response_model=chat_schema.Texts)
async def create_chat(
    payload: chat_schema.Text,
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    """
    Send a question, create a conversation and get an AI-generated response.

    Parameters:
        payload (Text): Contains the question text and model configuration
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        Texts: The AI-generated response

    Raises:
        HTTPException: If user is not authorized
    """
    chat = Chat(user_id=user.id)
    db.add(chat)
    # Guardar la pregunta
    n_orden = (
        (await db.execute(select(Message.order_number).where(Message.chat_id == chat.id)))
        .scalars()
        .all()
    )
    n_orden = max(n_orden) + 1 if n_orden else 1

    stmt = select(Model).where(Model.ia_name == payload.model)
    result = await db.execute(stmt)
    model = result.scalars().first()
    
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    message = Message(chat_id=chat.id, order_number=n_orden, content=payload.text, model_id=model.id)
    db.add(message)
    # Llamada a servicio externo (placeholder)
    respuesta = (
        f"Respuesta simulada a '{payload.text}' usando el modelo {payload.model}"
    )
    # Guardar la respuesta
    n_orden += 1
    response_message = Message(chat_id=chat.id, order_number=n_orden, content=respuesta)
    db.add(response_message)
    await db.commit()
    await db.refresh(response_message)
    return {"text": respuesta}


@router.put("/chats", response_model=List[chat_schema.Texts])
async def import_conversation(
    payload: List[chat_schema.Texts],
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    """
    Import a full conversation.

    Parameters:
        payload (List[Texts]): List of messages to import into the chat
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        Tuple[UUID, List[Texts]]: The ID of the new chat and the imported messages

    Raises:

    """
    chat = Chat(user_id=user.id, titulo="Imported Chat")
    db.add(chat)
    # Insertar nuevos mensajes
    for i, msg in enumerate(payload, start=1):
        db.add(Message(chat_id=chat.id, order_number=i, content=msg.text))
    await db.commit()
    return chat.id, payload


@router.delete("/chats/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_conversation(
    chat_id: uuid.UUID,
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    """
    Delete a specific chat conversation and all its messages.

    Parameters:
        chat_id (UUID): The unique identifier of the chat to delete
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        None: Returns 204 No Content on success

    Raises:
        HTTPException: If chat is not found or user is not authorized
    """
    chat = await db.get(Chat, chat_id)
    if not chat or chat.user_id != user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    await db.delete(chat)
    await db.commit()
    return None
