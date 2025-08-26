# /api/routers/chats.py
from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from typing import List

from db import session, models
from schemas import chat as chat_schema
from api.dependencies import get_current_user

router = APIRouter()


@router.patch(
    "/chats/{chat_id}", response_model=chat_schema.MessageContent, tags=["Chats"]
)
def ask_question(
    chat_id: int,
    payload: chat_schema.MessagePayload,
    current_user: models.User = Depends(get_current_user),
):
    # Placeholder for chat logic: find chat, send to AI model, save, and return response
    return {"text": f"This is a sample response to '{payload.text}'"}


@router.get(
    "/chats/{chat_id}", response_model=List[chat_schema.MessageContent], tags=["Chats"]
)
def get_conversation(
    chat_id: int, current_user: models.User = Depends(get_current_user)
):
    # Placeholder: fetch all messages for the given chat_id if it belongs to the current user
    return [{"text": "Hello!"}, {"text": "How can I help you today?"}]


@router.delete(
    "/chats/{chat_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Chats"]
)
def delete_conversation(
    chat_id: int, current_user: models.User = Depends(get_current_user)
):
    # Placeholder for chat deletion logic
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put(
    "/chats/{chat_id}", response_model=List[chat_schema.MessageContent], tags=["Chats"]
)
def import_conversation(
    chat_id: int,
    messages: List[chat_schema.MessageContent],
    current_user: models.User = Depends(get_current_user),
):
    # Placeholder for importing messages into an existing chat
    return messages


@router.get(
    "/conversations", response_model=chat_schema.ConversationList, tags=["Chats"]
)
def get_conversation_list(current_user: models.User = Depends(get_current_user)):
    # Placeholder: fetch all chat titles and IDs for the current user
    convs = {
        f"conversation{i + 1}": {"idChat": f"ID{i + 1}", "title": f"Title {i + 1}"}
        for i in range(3)
    }
    return {"conversations": convs}
