# /api/routers/chats.py
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

from db.models import User, Chat
from schemas import chat as chat_schema
from auth.users import fastapi_users

router = APIRouter()

@router.get("/conversations", response_model=chat_schema.ConversationList)
async def get_user_conversations(user: User = Depends(fastapi_users.current_user(active=True))):
    convs = {
        f"conversation{i+1}": {"idChat": f"ID{i+1}", "Título": f"Título {i+1}"}
        for i, chat in enumerate(user.chats or [])
    }
    return {"conversations": convs}

@router.patch("/chats/{chat_id}", response_model=chat_schema.Texts)
async def ask_question_to_chat(chat_id: int, payload: chat_schema.Text, user: User = Depends(fastapi_users.current_user(active=True))):
    return {"text": f"Respuesta a '{payload.text}' usando el modelo {payload.model}"}

@router.get("/chats/{chat_id}", response_model=List[chat_schema.Texts])
async def get_full_conversation(chat_id: int, user: User = Depends(fastapi_users.current_user(active=True))):
    return [{"text": "Mensaje 1 de la conversación"}, {"text": "Mensaje 2"}]

@router.delete("/chats/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_conversation(chat_id: int, user: User = Depends(fastapi_users.current_user(active=True))):
    return None

@router.put("/chats/{chat_id}", response_model=List[chat_schema.Texts])
async def import_conversation(chat_id: int, payload: List[chat_schema.Texts], user: User = Depends(fastapi_users.current_user(active=True))):
    return payload