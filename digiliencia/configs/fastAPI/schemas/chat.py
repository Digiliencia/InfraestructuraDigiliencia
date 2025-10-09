# /schemas/chat.py
from pydantic import BaseModel
from typing import List


class Text(BaseModel):
    model: str
    text: str


class ChatCreate(BaseModel):
    tittle: str
    ia_prompt: str = ""


class Texts(BaseModel):
    text: str


class message(BaseModel):
    id: str
    order_number: int
    content: str
    model: str


class Captcha(BaseModel):
    captcha: str


class ConversationSummary(BaseModel):
    idChat: str
    tittle: str
    ia_prompt: str = ""


class ConversationFull(ConversationSummary):
    messages: List[message]


class ConversationSummaryList(BaseModel):
    conversations: List[ConversationSummary]


class ConversationList(BaseModel):
    conversations: List[ConversationFull]


class ModelList(BaseModel):
    models: dict
