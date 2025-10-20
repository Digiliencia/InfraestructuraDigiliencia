# /api/routers/chats.py
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import User, Chat, Message, IAPrompt
from schemas import chat as chat_schema
from auth.users import fastapi_users
from db.session import get_db


# Crear una dependencia reutilizable para el usuario actual
current_user = fastapi_users.current_user(active=True)

router = APIRouter(dependencies=[Depends(current_user)])


@router.get(
    "/conversations",
    response_model=chat_schema.ConversationSummaryList,
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
async def get_user_chat_list(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationSummaryList:
    """
    Retrieve a summary for the authenticated user.

    This endpoint returns a list of chat summaries associated with the
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
        ConversationSummaryList: Dictionary containing:
            - conversations (dict): Map of conversation IDs to their details
                - idChat (UUID): Unique identifier for the chat
                - tittle (str): Title/name of the conversation
                - ia_prompt (str): IA prompt associated with the conversation

    Example:
        ```json
        {
            "conversations": {
                "conversation1": {
                    "idChat": "550e8400-e29b-41d4-a716-446655440000",
                    "tittle": "General Questions",
                    "ia_prompt": "What is the capital of France?"
                },
                "conversation2": {
                    "idChat": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
                    "tittle": "Technical Support",
                    "ia_prompt": "How do I reset my password?"
                }
            }
        }
        ```
    """
    result = await db.execute(select(Chat).where(Chat.user_id == user.id))
    chats = result.scalars().all()
    summary = [
        chat_schema.ConversationSummary(
            idChat=str(chat.id), tittle=str(chat.tittle), ia_prompt=chat.ia_prompt
        )
        for chat in chats
    ]
    return chat_schema.ConversationSummaryList(conversations=summary)


@router.get("/chats/{chat_id}", response_model=chat_schema.ConversationFull)
async def get_full_conversation(
    chat_id: uuid.UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationFull:
    """
    Retrieve a full conversation by its ID.

    Parameters:
        chat_id (UUID): The unique identifier of the chat
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        ConversationFull: List of messages in the conversation and the summary

    Raises:
        HTTPException: If chat is not found or user is not authorized
    """
    chat = await db.get(Chat, chat_id)
    if chat is None or chat.user_id != user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    result = await db.execute(
        select(Message).where(Message.chat_id == chat_id).order_by(Message.order_number)
    )
    messages = result.scalars().all()
    conversations = chat_schema.ConversationFull(
        idChat=chat.id,
        tittle=chat.tittle,
        ia_prompt=chat.ia_prompt_id,
        messages=[
            chat_schema.message(
                id=msg.id,
                order_number=msg.order_number,
                content=msg.content,
                model_id=msg.model_id,
            )
            for msg in messages
        ],
    )
    return conversations


@router.patch("/chats/{chat_id}", response_model=chat_schema.Texts)
async def ask_question_to_chat(
    chat_id: uuid.UUID,
    payload: chat_schema.Text,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.Texts:
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
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    if not chat.user_id == user.id:
        raise HTTPException(
            status_code=403, detail="Not authorized to access this chat"
        )
    # Guardar la pregunta
    order_number = (
        (
            await db.execute(
                select(Message.order_number).where(Message.chat_id == chat_id)
            )
        )
        .scalars()
        .all()
    )
    order_number = max(order_number) + 1 if order_number else 1
    message = Message(chat_id=chat_id, order_number=order_number, content=payload.text)
    db.add(message)
    await db.commit()
    await db.refresh(message)
    # Llamada a servicio externo (placeholder)
    respuesta = (
        f"Respuesta simulada a '{payload.text}' usando el modelo {payload.model_id}"
    )
    # Guardar la respuesta
    order_number += 1
    response_message = Message(
        chat_id=chat_id, order_number=order_number, content=respuesta
    )
    db.add(response_message)
    await db.commit()
    await db.refresh(response_message)
    return chat_schema.Texts(text=respuesta)


@router.patch(
    "/chats",
    status_code=status.HTTP_201_CREATED,
    response_model=chat_schema.ConversationSummary,
)
async def create_chat(
    payload: chat_schema.ChatCreate,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    """
    Create a conversation.

    Parameters:
        payload (ChatCreate): Contains the template for the AI prompt and title.
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        ConversationSummary: a summary of the chat

    Raises:
        HTTPException: If user is not authorized
    """

    if not payload.ia_prompt:
        ia_prompt = await db.get(
            IAPrompt, "76f81605-08ac-4694-8122-18f6958c8797"
        )  # default
    else:
        ia_prompt = await db.get(IAPrompt, payload.ia_prompt)
    if not ia_prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid ia_prompt: The specified prompt does not exist",
        )
    chat = Chat(user_id=user.id, ia_prompt=ia_prompt, tittle=payload.tittle)
    db.add(chat)
    await db.commit()
    return chat_schema.ConversationSummary(
        idChat=UUID(str(chat.id)),
        tittle=str(chat.tittle),
        ia_prompt=UUID(str(ia_prompt.id)),
    )


@router.put("/chats", response_model=List[chat_schema.Texts])
async def import_conversation(
    payload: List[chat_schema.Texts],
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> tuple[UUID, List[chat_schema.Texts]]:
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
    chat = Chat(user_id=user.id, tittle="Imported Chat")
    db.add(chat)
    # Insertar nuevos mensajes
    for i, msg in enumerate(payload, start=1):
        db.add(Message(chat_id=chat.id, order_number=i, content=msg.text))
    await db.commit()
    return UUID(str(chat.id)), payload


@router.delete("/chats/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_conversation(
    chat_id: UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> None:
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
    if chat is None or not chat.user_id.is_(user.id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    await db.delete(chat)
    await db.commit()
    return None
