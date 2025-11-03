# /api/routers/chats.py
"""
This module defines the API routes for chat conversation management.

It includes endpoints for creating, retrieving, updating, and deleting chats
and their associated messages. All endpoints in this router require user
authentication.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func

from core.endpoints import CONVERSATIONS, CHATS_PATH
from db.models import User, Chat, Message, IAPrompt
from schemas import chat as chat_schema
from auth.users import fastapi_users
from db.session import get_db
import redis.asyncio as redis
from core.redis import get_redis

# Reusable dependency for the currently authenticated, active user.
current_user = fastapi_users.current_user(active=True)

router = APIRouter(dependencies=[Depends(current_user)])


@router.get(
    CONVERSATIONS,
    response_model=chat_schema.ConversationSummaryList,
    summary="List User Conversations",
    description="Retrieve a list of summaries for all conversations belonging to the authenticated user, sorted by creation date.",
    response_description="A list of conversation summaries.",
    status_code=status.HTTP_202_ACCEPTED
    responses={
        202: {
            "description": "A list of the user's conversation summaries.",
            "content": {
                "application/json": {
                    "example": {
                        "conversations": [
                            {
                                "idChat": "550e8400-e29b-41d4-a716-446655440000",
                                "tittle": "General Questions",
                                "ia_prompt": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
                            }
                        ]
                    }
                }
            },
        },
        401: {"description": "User is not authenticated."},
    },
)
async def get_user_chat_list(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationSummaryList:
    """
    Retrieves a summary list of all chats for the authenticated user.

    Args:
        user (User): The currently authenticated user, injected by dependency.
        db (AsyncSession): The database session, injected by dependency.

    Returns:
        chat_schema.ConversationSummaryList: An object containing a list of
                                             conversation summaries.
    """
    stmt = select(Chat).where(Chat.user_id == user.id).order_by(Chat.id.desc())
    result = await db.execute(stmt)
    chats = result.scalars().all()

    summaries = [
        chat_schema.ConversationSummary(
            idChat=chat.id, tittle=chat.tittle, ia_prompt=chat.ia_prompt_id
        )
        for chat in chats
    ]
    return chat_schema.ConversationSummaryList(conversations={summary.idChat: summary for summary in summaries})


@router.get(
    f"{CHATS_PATH}/{{chat_id}}",
    response_model=chat_schema.ConversationFull,
    summary="Get Full Conversation Details",
    description="Retrieve the full details of a specific conversation, including all messages, by its unique ID.",
    response_description="The full conversation object with its message history.",
    responses={
        200: {"description": "The full conversation object."},
        401: {"description": "User is not authenticated."},
        404: {
            "description": "The chat was not found or the user is not authorized to view it."
        },
    },
)
async def get_full_conversation(
    chat_id: UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
    status_code=status.HTTP_202_ACCEPTED
) -> chat_schema.ConversationFull:
    """
    Retrieves a full conversation, including its messages, by its ID.

    Args:
        chat_id (UUID): The unique identifier of the chat to retrieve.
        user (User): The currently authenticated user.
        db (AsyncSession): The database session.

    Returns:
        chat_schema.ConversationFull: The complete conversation object.

    Raises:
        HTTPException: 404 Not Found if the chat does not exist or does not
                       belong to the authenticated user.
    """
    chat = await db.get(Chat, chat_id)
    if chat is None or chat.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )

    stmt = (
        select(Message).where(Message.chat_id == chat_id).order_by(Message.order_number)
    )
    result = await db.execute(stmt)
    messages = result.scalars().all()

    return chat_schema.ConversationFull(
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


@router.patch(
    f"{CHATS_PATH}/{{chat_id}}",
    response_model=chat_schema.Texts,
    summary="Send Message to Chat",
    description="Sends a user's message to an existing chat, gets a simulated AI response, and saves both to the conversation history.",
    response_description="The AI-generated response text.",
    responses={
        200: {"description": "The AI-generated response."},
        401: {"description": "User is not authenticated."},
        404: {
            "description": "The chat was not found or the user is not authorized to access it."
        },
    },
)
@router.patch(
    f"{CHATS_PATH}/{{chat_id}}",
    response_model=chat_schema.Texts,
    summary="Send Message to Chat",
    description=(
        "Sends a user's message to an existing chat, gets a simulated AI "
        "response, and saves both to the conversation history. This endpoint "
        "uses a lock to prevent concurrent messages to the same chat. If a "
        "message is already being processed, it will return a 409 Conflict."
    ),
    response_description="The AI-generated response text.",
    responses={
        200: {"description": "The AI-generated response."},
        401: {"description": "User is not authenticated."},
        404: {
            "description": "The chat was not found or the user is not authorized to access it."
        },
        409: {"description": "A request for this chat is already being processed."},
    },
)
async def ask_question_to_chat(
    chat_id: UUID,
    payload: chat_schema.Text,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis),
) -> chat_schema.Texts:
    """
    Adds a user message to a chat and returns a simulated AI response.

    Args:
        chat_id (UUID): The ID of the chat to add a message to.
        payload (chat_schema.Text): The request body containing the user's text.
        user (User): The currently authenticated user.
        db (AsyncSession): The database session.
        redis_client (redis.Redis): The Redis client for locking.

    Returns:
        chat_schema.Texts: An object containing the simulated AI response text.

    Raises:
        HTTPException: 404 Not Found if the chat does not exist or does not
                       belong to the authenticated user.
        HTTPException: 409 Conflict if a message to this chat is already
                       being processed.
    """
    lock_key = f"chat_lock:{chat_id}"
    is_lock_acquired = await redis_client.set(lock_key, "processing", nx=True, ex=60)

    if not is_lock_acquired:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A request for this chat is already being processed.",
        )
    try:
        chat = await db.get(Chat, chat_id)
        if chat is None or chat.user_id != user.id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
            )

        # Get the next available order number for the message
        max_order_stmt = select(func.max(Message.order_number)).where(
            Message.chat_id == chat_id
        )
        last_order_result = await db.execute(max_order_stmt)
        last_order = last_order_result.scalar_one_or_none() or 0

        # Save the user's question
        user_message = Message(
            chat_id=chat_id,
            order_number=last_order + 1,
            content=payload.text,
            model_id=payload.model_id,
        )
        db.add(user_message)

        # Simulate external AI service call
        ai_response_text = (
            f"Simulated response to '{payload.text}' using model {payload.model_id}"
        )

        # Save the AI's response
        ai_message = Message(
            chat_id=chat_id, order_number=last_order + 2, content=ai_response_text
        )
        db.add(ai_message)

        await db.commit()
        return chat_schema.Texts(text=ai_response_text)
    finally:
        await redis_client.delete(lock_key)


@router.patch(
    CHATS_PATH,
    status_code=status.HTTP_201_CREATED,
    response_model=chat_schema.ConversationSummary,
    summary="Create New Chat",
    description="Creates a new, empty chat conversation with a title and an associated AI prompt (template).",
    response_description="A summary of the newly created chat.",
    responses={
        201: {"description": "The chat was created successfully."},
        400: {"description": "The provided `ia_prompt` UUID does not exist."},
        401: {"description": "User is not authenticated."},
    },
)
async def create_chat(
    payload: chat_schema.ChatCreate,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationSummary:
    """
    Creates a new chat for the authenticated user.

    If no `ia_prompt` is provided, a default prompt will be assigned.

    Args:
        payload (chat_schema.ChatCreate): The request body containing the title
                                          and optional prompt ID.
        user (User): The currently authenticated user.
        db (AsyncSession): The database session.

    Returns:
        chat_schema.ConversationSummary: A summary of the created chat.

    Raises:
        HTTPException: 400 Bad Request if the provided `ia_prompt` ID is invalid.
    """
    if payload.ia_prompt:
        ia_prompt = await db.get(IAPrompt, payload.ia_prompt)
    else:
        stmt = select(IAPrompt).limit(1)
        result = await db.execute(stmt)
        ia_prompt = result.scalar_one_or_none()

    if not ia_prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid ia_prompt: The specified prompt does not exist or no default is available.",
        )

    chat = Chat(user_id=user.id, ia_prompt_id=ia_prompt.id, tittle=payload.tittle)
    db.add(chat)
    await db.commit()
    await db.refresh(chat)

    return chat_schema.ConversationSummary(
        idChat=chat.id,
        tittle=chat.tittle,
        ia_prompt=ia_prompt.id,
    )


@router.put(
    CHATS_PATH,
    response_model=chat_schema.ConversationSummary,
    summary="Import Conversation as New Chat",
    description="Creates a new chat by importing a list of messages, a title, and an optional prompt.",
    response_description="A summary of the newly created chat.",
)
async def import_conversation(
    payload: chat_schema.ConversationImport,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationSummary:
    """
    Creates a new chat for the user by importing an existing conversation.

    Args:
        payload (chat_schema.ConversationImport): The object containing the title,
                                                  a list of texts, and an
                                                  optional prompt ID.
        user (User): The currently authenticated user.
        db (AsyncSession): The database session.

    Returns:
        chat_schema.ConversationSummary: A summary of the newly created chat.
    """
    if payload.ia_prompt:
        ia_prompt = await db.get(IAPrompt, payload.ia_prompt)
        if not ia_prompt:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The provided 'ia_prompt' UUID does not exist.",
            )
    else:
        stmt = select(IAPrompt).limit(1)
        result = await db.execute(stmt)
        ia_prompt = result.scalar_one_or_none()
        if not ia_prompt:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Default IA prompt not found. Database may not be seeded.",
            )

    chat = Chat(user_id=user.id, tittle=payload.tittle, ia_prompt_id=ia_prompt.id)
    db.add(chat)

    try:
        await db.flush()
    except Exception:
        await db.rollback()
        raise

    for i, msg in enumerate(payload.texts, start=1):
        new_msg = Message(chat_id=chat.id, order_number=i, content=msg.text)
        db.add(new_msg)

    await db.commit()
    await db.refresh(chat)

    return chat_schema.ConversationSummary(
        idChat=chat.id, tittle=chat.tittle, ia_prompt=chat.ia_prompt_id
    )


@router.delete(
    f"{CHATS_PATH}/{{chat_id}}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a Chat",
    description="Permanently deletes a chat and all of its associated messages by its unique ID.",
    response_description="No content is returned on successful deletion.",
    responses={
        204: {"description": "The chat was successfully deleted."},
        401: {"description": "User is not authenticated."},
        404: {
            "description": "The chat was not found or the user is not authorized to delete it."
        },
    },
)
async def delete_conversation(
    chat_id: UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> None:
    """
    Deletes a specific chat conversation.

    Args:
        chat_id (UUID): The unique identifier of the chat to delete.
        user (User): The currently authenticated user.
        db (AsyncSession): The database session.

    Returns:
        None

    Raises:
        HTTPException: 404 Not Found if the chat does not exist or does not
                       belong to the authenticated user.
    """
    chat = await db.get(Chat, chat_id)

    if chat is None or chat.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )

    await db.delete(chat)
    await db.commit()
    return None
