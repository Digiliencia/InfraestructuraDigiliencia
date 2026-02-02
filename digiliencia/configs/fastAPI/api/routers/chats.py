# /api/routers/chats.py
"""
This module defines the API routes for chat conversation management.

It provides endpoints for creating, retrieving, updating, and deleting chats
and their associated messages. All endpoints strictly require user authentication.
"""

import asyncio
from typing import cast
from uuid import UUID

import redis.asyncio as redis
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from auth.users import fastapi_users
from core.endpoints import CHATS_PATH, CONVERSATIONS
from core.redis import get_redis
from db.models import Chat, AIPrompt, Message, User
from db.session import get_db
from schemas import chat as chat_schema

# Reusable dependency for the currently authenticated, active user.
current_user = fastapi_users.current_user(active=True)

router = APIRouter(dependencies=[Depends(current_user)])


@router.get(
    CONVERSATIONS,
    response_model=chat_schema.ConversationSummaries,
    summary="List User Conversations",
    description="Retrieve a list of summaries for all conversations belonging to the authenticated user.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Successfully retrieved the list of conversation summaries."
        },
        401: {"description": "User is not authenticated."},
    },
)
async def get_user_chat_list(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationSummaries:
    """
    Retrieves a summary list of all chats for the authenticated user.
    """
    query = select(Chat).where(Chat.user_id == user.id).order_by(Chat.id.desc())
    result = await db.execute(query)
    chats = result.scalars().all()

    summaries = tuple(
        chat_schema.ConversationSummary(
            id=chat.id,
            title=str(chat.title),
            ai_prompt_id=chat.ai_prompt_id,
        )
        for chat in chats
    )

    return chat_schema.ConversationSummaries(conversations=summaries)


@router.get(
    f"{CHATS_PATH}/{{chat_id}}",
    response_model=chat_schema.ConversationFull,
    summary="Get Full Conversation Details",
    description="Retrieve the full details of a specific conversation, including the complete message history.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Successfully retrieved the full conversation object."},
        404: {"description": "Chat not found or access denied."},
    },
)
async def get_full_conversation(
    chat_id: UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationFull:
    """
    Retrieves a full conversation and its messages by ID.
    """
    chat = await db.get(Chat, chat_id)
    if chat is None or chat.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )

    query = (
        select(Message).where(Message.chat_id == chat_id).order_by(Message.order_number)
    )
    result = await db.execute(query)
    messages = result.scalars().all()

    return chat_schema.ConversationFull(
        id=chat.id,
        title=str(chat.title),
        ai_prompt_id=chat.ai_prompt_id,
        messages=tuple(
            chat_schema.Message(
                id=msg.id,
                order_number=cast(int, msg.order_number),
                content=str(msg.content),
                model_id=msg.model_id,
            )
            for msg in messages
        ),
    )


@router.patch(
    f"{CHATS_PATH}/{{chat_id}}",
    response_model=chat_schema.AIResponse,
    summary="Send Message to Chat",
    description="Sends a user message, generates a simulated AI response, and persists both.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Message processed successfully."},
        409: {"description": "Concurrent request conflict (Chat is busy)."},
    },
)
async def ask_question_to_chat(
    chat_id: UUID,
    payload: chat_schema.MessageInput,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis),
) -> chat_schema.AIResponse:
    """
    Processes a user's message and generates an AI response using Redis locking.
    """
    lock_key = f"chat_lock:{chat_id}"
    is_lock_acquired = await redis_client.set(lock_key, "processing", nx=True, ex=60)

    if not is_lock_acquired:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A request for this chat is already being processed. Please wait.",
        )

    try:
        chat = await db.get(Chat, chat_id)
        if chat is None or chat.user_id != user.id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
            )

        max_order_query = select(func.max(Message.order_number)).where(
            Message.chat_id == chat_id
        )
        max_order_result = await db.execute(max_order_query)
        last_order = max_order_result.scalar_one_or_none() or 0

        # 1. Save User Message
        user_message = Message(
            chat_id=chat_id,
            order_number=last_order + 1,
            content=payload.content,
            model_id=payload.model_id,
        )
        db.add(user_message)

        # 2. Simulate AI
        ai_response_text = (
            f"Simulated response to '{payload.content}' using model {payload.model_id}"
        )
        await asyncio.sleep(0.2)

        # 3. Save AI Message
        ai_message = Message(
            chat_id=chat_id, order_number=last_order + 2, content=ai_response_text
        )
        db.add(ai_message)

        await db.commit()
        return chat_schema.AIResponse(text=ai_response_text)
    finally:
        await redis_client.delete(lock_key)


@router.patch(
    CHATS_PATH,
    response_model=chat_schema.ConversationSummary,
    summary="Create New Chat",
    description="Creates a new chat conversation.",
    status_code=status.HTTP_201_CREATED,
)
async def create_chat(
    payload: chat_schema.ChatCreate,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationSummary:
    """
    Initializes a new chat session.
    """
    ai_prompt = None

    if payload.ai_prompt_id:
        ai_prompt = await db.get(AIPrompt, payload.ai_prompt_id)
    else:
        query = select(AIPrompt).limit(1)
        result = await db.execute(query)
        ai_prompt = result.scalar_one_or_none()

    if not ai_prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid AI prompt: Prompt not found or no default available.",
        )

    chat = Chat(user_id=user.id, ai_prompt_id=ai_prompt.id, title=payload.title)
    db.add(chat)
    await db.commit()
    await db.refresh(chat)

    return chat_schema.ConversationSummary(
        id=chat.id,
        title=str(chat.title),
        ai_prompt_id=chat.ai_prompt_id,
    )


@router.put(
    CHATS_PATH,
    response_model=chat_schema.ConversationSummary,
    summary="Import Conversation",
    description="Creates a new chat by bulk importing a list of message texts.",
    status_code=status.HTTP_201_CREATED,
)
async def import_conversation(
    payload: chat_schema.ConversationImport,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationSummary:
    """
    Imports an existing conversation structure into a new chat.
    """
    if payload.ai_prompt_id:
        ai_prompt = await db.get(AIPrompt, payload.ai_prompt_id)
        if not ai_prompt:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The provided 'ai_prompt_id' UUID does not exist.",
            )
    else:
        query = select(AIPrompt).limit(1)
        result = await db.execute(query)
        ai_prompt = result.scalar_one_or_none()
        if not ai_prompt:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Default AI prompt configuration missing.",
            )

    chat = Chat(user_id=user.id, title=payload.title, ai_prompt_id=ai_prompt.id)
    db.add(chat)

    await db.flush()

    new_messages = [
        Message(chat_id=chat.id, order_number=i, content=msg.text)
        for i, msg in enumerate(payload.texts, start=1)
    ]
    db.add_all(new_messages)

    await db.commit()
    await db.refresh(chat)

    return chat_schema.ConversationSummary(
        id=chat.id,
        title=str(chat.title),
        ai_prompt_id=chat.ai_prompt_id,
    )


@router.delete(
    f"{CHATS_PATH}/{{chat_id}}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Chat",
    description="Permanently removes a chat and all associated messages.",
)
async def delete_conversation(
    chat_id: UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> None:
    """
    Deletes a chat by ID.
    """
    chat = await db.get(Chat, chat_id)

    if chat is None or chat.user_id != user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )

    await db.delete(chat)
    await db.commit()
