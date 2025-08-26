# /schemas/chat.py
from pydantic import BaseModel
from typing import List, Dict


class MessagePayload(BaseModel):
    model: str
    text: str


class MessageContent(BaseModel):
    text: str


class ConversationInfo(BaseModel):
    idChat: str
    title: str


class ConversationList(BaseModel):
    conversations: Dict[str, ConversationInfo]


class Captcha(BaseModel):
    captcha: str
