# /schemas/chat.py
"""
This module defines the Pydantic models (schemas) for the Chat API.

These schemas handle data validation and serialization for chat conversations,
messages, AI models, and templates.
"""

from typing import Optional, Tuple
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class MessageInput(BaseModel):
    """
    Schema for a new message sent by the user.

    This is used when sending a message to an existing chat conversation.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "content": "How does recursion work in Python?",
                    "model_id": "68b92fa2-fe59-4181-99a5-032190d68a73",
                }
            ]
        }
    )

    content: str = Field(
        ...,
        min_length=1,
        description="The text content of the user's message",
        examples=["What is the difference between a list and a tuple?"],
    )
    model_id: Optional[UUID] = Field(
        None,
        description="UUID of the AI model to use for generating the response. If not specified, the default model is used.",
        examples=["68b92fa2-fe59-4181-99a5-032190d68a73"],
    )


class ChatCreate(BaseModel):
    """
    Schema for creating a new chat conversation.

    Use this to initialize a new chat session with an optional AI template.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "title": "Python Development Questions",
                    "ai_prompt_id": "76f81605-08ac-4694-8122-18f6958c8797",
                }
            ]
        }
    )

    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Descriptive title for the conversation",
        examples=["Machine Learning Project", "Web Development Queries"],
    )
    ai_prompt_id: Optional[UUID] = Field(
        None,
        description="UUID of the AI template/prompt to use. If not specified, the default template is used.",
        examples=["76f81605-08ac-4694-8122-18f6958c8797"],
    )


class AIResponse(BaseModel):
    """
    Schema representing a text response from the AI.

    This is returned after sending a message to a chat.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "text": "Recursion is a programming technique where a function calls itself..."
                }
            ]
        }
    )

    text: str = Field(
        ...,
        description="Text content of the AI-generated response",
        examples=["Here is my detailed answer to your question..."],
    )


class Message(BaseModel):
    """
    Schema representing a single message within a conversation history.

    Messages are ordered sequentially and can be from either the user or the AI.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "a3bb189e-8bf9-4456-8888-5ca698b0125e",
                    "order_number": 1,
                    "content": "What is FastAPI?",
                    "model_id": "68b92fa2-fe59-4181-99a5-032190d68a73",
                }
            ]
        }
    )

    id: UUID = Field(..., description="Unique identifier for the message")
    order_number: int = Field(
        ...,
        description="Sequential order of the message in the conversation (starting from 1)",
        ge=1,
    )
    content: str = Field(..., description="Text content of the message")
    model_id: Optional[UUID] = Field(
        None,
        description="UUID of the model used to generate this message (only for AI messages)",
    )


class Captcha(BaseModel):
    """Schema for captcha verification."""

    captcha: str = Field(..., description="Captcha verification token")


class ConversationSummary(BaseModel):
    """
    Schema for a high-level summary of a chat conversation.

    Used when listing all conversations for a user.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                    "title": "Machine Learning Project",
                    "ai_prompt_id": "76f81605-08ac-4694-8122-18f6958c8797",
                }
            ]
        }
    )

    id: UUID = Field(..., description="Unique identifier for the conversation")
    title: str = Field(..., description="Title of the conversation")
    ai_prompt_id: UUID = Field(..., description="UUID of the AI template/prompt used")


class ConversationFull(ConversationSummary):
    """
    Schema for a detailed chat conversation including message history.

    Extends ConversationSummary with the complete message history.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                    "title": "Machine Learning Project",
                    "ai_prompt_id": "76f81605-08ac-4694-8122-18f6958c8797",
                    "messages": [
                        {
                            "id": "a3bb189e-8bf9-4456-8888-5ca698b0125e",
                            "order_number": 1,
                            "content": "How do I get started with machine learning?",
                            "model_id": None,
                        },
                        {
                            "id": "b4cc289f-9cf0-5567-9999-6db709c0236f",
                            "order_number": 2,
                            "content": "To get started with machine learning, I recommend...",
                            "model_id": "68b92fa2-fe59-4181-99a5-032190d68a73",
                        },
                    ],
                }
            ]
        }
    )

    messages: Tuple[Message, ...] = Field(
        ...,
        description="Complete message history for the conversation, ordered by order_number",
    )


class ConversationSummaries(BaseModel):
    """Schema for a list of conversation summaries."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "conversations": [
                        {
                            "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                            "title": "ML Project",
                            "ai_prompt_id": "76f81605-08ac-4694-8122-18f6958c8797",
                        },
                        {
                            "id": "e36bc09a-47bb-3261-9456-1eb608b1125d",
                            "title": "Web Development",
                            "ai_prompt_id": "76f81605-08ac-4694-8122-18f6958c8797",
                        },
                    ]
                }
            ]
        }
    )

    conversations: Tuple[ConversationSummary, ...] = Field(
        ..., description="List of conversation summaries for the user"
    )


class ConversationImport(BaseModel):
    """
    Schema for importing an existing conversation structure.

    Use this to bulk-import messages into a new conversation.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "title": "Imported Conversation",
                    "ai_prompt_id": "76f81605-08ac-4694-8122-18f6958c8797",
                    "texts": [
                        {"text": "First user question"},
                        {"text": "AI response"},
                        {"text": "Second user question"},
                    ],
                }
            ]
        }
    )

    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Title for the conversation to import",
    )
    ai_prompt_id: Optional[UUID] = Field(
        None,
        description="UUID of the AI template/prompt. If not specified, the default is used.",
    )
    texts: Tuple[AIResponse, ...] = Field(
        ..., description="Ordered list of messages to import"
    )


class ModelSummary(BaseModel):
    """
    Schema for an available AI Model.

    Represents a language model that can be used for generating responses.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"id": "68b92fa2-fe59-4181-99a5-032190d68a73", "name": "GPT-4"}
            ]
        }
    )

    id: UUID = Field(..., description="Unique identifier for the model")
    name: str = Field(
        ..., description="Name of the model (e.g., GPT-4, Claude 3, Llama 2)"
    )


class Models(BaseModel):
    """Schema for returning a list of available AI models."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "models": [
                        {"id": "68b92fa2-fe59-4181-99a5-032190d68a73", "name": "GPT-4"},
                        {
                            "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                            "name": "Claude 3",
                        },
                    ]
                }
            ]
        }
    )

    models: Tuple[ModelSummary, ...] = Field(
        ..., description="List of AI models available in the system"
    )


class TemplateSummary(BaseModel):
    """
    Schema for an available AI Prompt Template.

    Templates define the AI's behavior and personality for a conversation.
    """

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "76f81605-08ac-4694-8122-18f6958c8797",
                    "name": "General Assistant",
                    "description": "A helpful assistant for general queries",
                }
            ]
        }
    )

    id: UUID = Field(..., description="Unique identifier for the template")
    name: str = Field(
        ..., description="Name of the template (e.g., General Assistant, Code Tutor)"
    )
    description: str = Field(
        ..., description="Description of the template's purpose and behavior"
    )


class Templates(BaseModel):
    """Schema for returning a list of available templates."""

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "templates": [
                        {
                            "id": "76f81605-08ac-4694-8122-18f6958c8797",
                            "name": "General Assistant",
                            "description": "A helpful assistant for general queries",
                        },
                        {
                            "id": "87g92fa2-ge69-5282-00b6-143301e79a84",
                            "name": "Programming Tutor",
                            "description": "Specialized in teaching programming concepts",
                        },
                    ]
                }
            ]
        }
    )

    templates: Tuple[TemplateSummary, ...] = Field(
        ..., description="List of available AI templates/prompts"
    )
