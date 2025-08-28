# /schemas/chat.py
from pydantic import BaseModel
from typing import Dict, List

class Text(BaseModel):
    model: str
    text: str

class Texts(BaseModel):
    text: str

class Captcha(BaseModel):
    captcha: str

class ConversationDetail(BaseModel):
    idChat: str
    Título: str

class ConversationList(BaseModel):
    conversations: Dict[str, ConversationDetail]