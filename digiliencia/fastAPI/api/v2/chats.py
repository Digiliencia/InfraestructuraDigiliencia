# /api/v2/chats.py
from uuid import UUID
from fastapi import APIRouter, Depends
from db.models import User
from db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
import redis.asyncio as redis
from core.redis import get_redis
from api.routers.chats import (
    get_user_chat_list,
    get_full_conversation,
    ask_question_to_chat,
    create_chat,
    import_conversation,
    delete_conversation,
    current_user,
)
from schemas import chat as chat_schema

router = APIRouter(dependencies=[Depends(current_user)])


# All paths start with /v2/chats to be consistent and avoid doubling
@router.get("/v2/chats/conversations", response_model=chat_schema.ConversationSummaries)
async def v2_get_user_chat_list(
    user: User = Depends(current_user), db: AsyncSession = Depends(get_db)
):
    return await get_user_chat_list(user, db)


@router.get("/v2/chats/{chat_id}", response_model=chat_schema.ConversationFull)
async def v2_get_full_conversation(
    chat_id: UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    return await get_full_conversation(chat_id, user, db)


@router.patch("/v2/chats/{chat_id}", response_model=chat_schema.AIResponse)
async def v2_ask_question_to_chat(
    chat_id: UUID,
    payload: chat_schema.MessageInput,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis),
):
    return await ask_question_to_chat(chat_id, payload, user, db, redis_client)


@router.patch(
    "/v2/chats", response_model=chat_schema.ConversationSummary, status_code=201
)
async def v2_create_chat(
    payload: chat_schema.ChatCreate,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    return await create_chat(payload, user, db)


@router.put(
    "/v2/chats", response_model=chat_schema.ConversationSummary, status_code=201
)
async def v2_import_conversation(
    payload: chat_schema.ConversationImport,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    return await import_conversation(payload, user, db)


@router.delete("/v2/chats/{chat_id}", status_code=204)
async def v2_delete_conversation(
    chat_id: UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
):
    return await delete_conversation(chat_id, user, db)
