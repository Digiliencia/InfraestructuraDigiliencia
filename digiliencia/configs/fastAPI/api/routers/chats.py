# /api/routers/chats.py
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import User, Chat, Message, Model
from schemas import chat as chat_schema
from auth.users import fastapi_users
from db.session import get_db

router = APIRouter()


@router.get("/conversations", response_model=chat_schema.ConversationList)
async def get_user_conversations(
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Chat).where(Chat.user_id == user.id))
    chats = result.scalars().all()
    convs = {
        f"conversation{chat.id}": {"idChat": str(chat.id), "Título": chat.titulo}
        for chat in chats
    }
    return {"conversations": convs}


@router.get("/chats/{chat_id}", response_model=List[chat_schema.Texts])
async def get_full_conversation(
    chat_id: int,
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    chat = await db.get(Chat, chat_id)
    if not chat or chat.user_id != user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    result = await db.execute(
        select(Message)
        .where(Message.chat_id == chat_id)
        .order_by(Message.n_orden)
    )
    messages = result.scalars().all()
    return [{"text": m.contenido} for m in messages]


@router.patch("/chats/{chat_id}", response_model=chat_schema.Texts)
async def ask_question_to_chat(
    chat_id: int,
    payload: chat_schema.Text,
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    chat = await db.get(Chat, chat_id)
    if not chat or chat.user_id != user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    # Guardar la pregunta
    n_orden = (
        await db.execute(select(Message.n_orden).where(Message.chat_id == chat_id))
    ).scalars().all()
    n_orden = max(n_orden) + 1 if n_orden else 1
    message = Message(chat_id=chat_id, n_orden=n_orden, contenido=payload.text)
    db.add(message)
    await db.commit()
    await db.refresh(message)
    # Llamada a servicio externo (placeholder)
    respuesta = f"Respuesta simulada a '{payload.text}' usando el modelo {payload.model}"
    # Guardar la respuesta
    n_orden += 1
    response_message = Message(chat_id=chat_id, n_orden=n_orden, contenido=respuesta)
    db.add(response_message)
    await db.commit()
    await db.refresh(response_message)
    return {"text": respuesta}


@router.put("/chats/{chat_id}", response_model=List[chat_schema.Texts])
async def import_conversation(
    chat_id: int,
    payload: List[chat_schema.Texts],
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    chat = await db.get(Chat, chat_id)
    if not chat or chat.user_id != user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    # Borrar mensajes anteriores
    await db.execute(
        Message.__table__.delete().where(Message.chat_id == chat_id)
    )
    # Insertar nuevos mensajes
    for i, msg in enumerate(payload, start=1):
        db.add(Message(chat_id=chat_id, n_orden=i, contenido=msg.text))
    await db.commit()
    return payload


@router.delete("/chats/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_conversation(
    chat_id: int,
    user: User = Depends(fastapi_users.current_user(active=True)),
    db: AsyncSession = Depends(get_db),
):
    chat = await db.get(Chat, chat_id)
    if not chat or chat.user_id != user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    await db.delete(chat)
    await db.commit()
    return None
