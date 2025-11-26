# /schemas/chat.py
"""
This module defines the Pydantic models (schemas) for the Chat API.

These schemas handle data validation and serialization for chat conversations,
messages, AI models, and templates.
"""

from typing import Optional, Tuple
from uuid import UUID

from pydantic import BaseModel, Field


class MessageInput(BaseModel):
    """
    Schema for a new message sent by the user.
    """

    content: str = Field(..., min_length=1, description="The message text.")
    model_id: Optional[UUID] = Field(None, description="The specific AI model to use.")


class ChatCreate(BaseModel):
    """
    Schema for creating a new chat conversation.
    """

    title: str = Field(..., min_length=1, max_length=255)
    ai_prompt_id: Optional[UUID] = Field(
        None, description="UUID of the AI Prompt/Template to use."
    )


class AIResponse(BaseModel):
    """Schema representing a text response from the AI."""

    text: str


class Message(BaseModel):
    """
    Schema representing a single message within a conversation history.
    """

    id: UUID
    order_number: int
    content: str
    model_id: Optional[UUID] = None


class Captcha(BaseModel):
    """Schema for captcha verification."""

    captcha: str


class ConversationSummary(BaseModel):
    """
    Schema for a high-level summary of a chat conversation.
    """

    id: UUID
    title: str
    ai_prompt_id: UUID


class ConversationFull(ConversationSummary):
    """
    Schema for a detailed chat conversation including message history.
    """

    messages: Tuple[Message, ...]


class ConversationSummaries(BaseModel):
    """Schema for a list of conversation summaries."""

    conversations: Tuple[ConversationSummary, ...]


class ConversationImport(BaseModel):
    """
    Schema for importing an existing conversation structure.
    """

    title: str = Field(..., min_length=1, max_length=255)
    ai_prompt_id: Optional[UUID] = None
    texts: Tuple[AIResponse, ...]


class ModelSummary(BaseModel):
    """
    Schema for an available AI Model.
    """

    id: UUID
    name: str


class Models(BaseModel):
    """Schema for returning a list of available AI models."""

    models: Tuple[ModelSummary, ...]


class TemplateSummary(BaseModel):
    """
    Schema for an available AI Prompt Template.
    """

    id: UUID
    name: str
    description: str


class Templates(BaseModel):
    """Schema for returning a list of available templates."""

    templates: Tuple[TemplateSummary, ...]
