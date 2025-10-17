# /schemas/chat.py
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class Text(BaseModel):
    model_id: Optional[UUID]
    text: str


class ChatCreate(BaseModel):
    tittle: str
    ia_prompt: Optional[UUID] = None


class Texts(BaseModel):
    text: str


class message(BaseModel):
    id: UUID
    order_number: int
    content: str
    model_id: Optional[UUID]


class Captcha(BaseModel):
    captcha: str


class ConversationSummary(BaseModel):
    idChat: UUID
    tittle: str
    ia_prompt: UUID


class ConversationFull(ConversationSummary):
    messages: List[message]


class ConversationSummaryList(BaseModel):
    conversations: List[ConversationSummary]


class ConversationList(BaseModel):
    conversations: List[ConversationFull]


class ModelSummary(BaseModel):
    idModel: UUID
    model_name: str


class ModelList(BaseModel):
    models: tuple[ModelSummary]


class TemplateSummary(BaseModel):
    idTemplate: UUID
    template_name: str
    template_description: str


class TemplateList(BaseModel):
    templates: tuple[TemplateSummary]
