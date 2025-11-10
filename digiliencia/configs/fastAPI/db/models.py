# /db/models.py
"""
This module defines the SQLAlchemy ORM models for the application's database schema.

It includes models for users, chat conversations, messages, AI prompts (templates),
and AI models. The relationships between these entities are also defined here.
"""

import uuid
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    JSON,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, declarative_base
import fastapi_users.db

# The declarative base class for all SQLAlchemy models in this application.
Base = declarative_base()


class User(fastapi_users.db.SQLAlchemyBaseUserTableUUID, Base):
    """
    Represents a user in the system.

    This model inherits from the `fastapi-users` base table, providing standard
    fields for authentication and user management (e.g., email, hashed_password).

    Relationships:
        - A one-to-many relationship to Chat (`chats`).
    """

    __tablename__ = "users"

    # Relationship to Chat: one user can have many chats.
    # `cascade="all, delete-orphan"` ensures that when a user is deleted,
    # all of their associated chats are also deleted.
    chats = relationship("Chat", back_populates="owner", cascade="all, delete-orphan")


class Chat(Base):
    """
    Represents a single chat conversation.

    Each chat is owned by a user and consists of a sequence of messages. It is
    also associated with an initial AI prompt template.

    Attributes:
        id (UUID): The primary key for the chat.
        tittle (str): The user-defined title of the conversation.
        user_id (UUID): A foreign key linking to the `users` table.
        ia_prompt_id (UUID): A foreign key linking to the `ia_prompts` table.

    Relationships:
        - A many-to-one relationship to User (`owner`).
        - A one-to-many relationship to Message (`messages`).
        - A many-to-one relationship to IAPrompt (`ia_prompt`).
    """

    __tablename__ = "chats"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tittle = Column(String(255), index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    ia_prompt_id = Column(UUID(as_uuid=True), ForeignKey("ia_prompts.id"))

    owner = relationship("User", back_populates="chats")
    messages = relationship(
        "Message", back_populates="chat", cascade="all, delete-orphan"
    )
    ia_prompt = relationship("IAPrompt", back_populates="chats")


class IAPrompt(Base):
    """
    Represents an AI prompt template.

    These are predefined system prompts that can be used to initialize a chat
    conversation with a specific context or persona for the AI.

    Attributes:
        id (UUID): The primary key for the prompt.
        prompt_name (str): The display name of the template.
        prompt (str): The actual system prompt text.
        prompt_description (str): A user-friendly description of the template.

    Relationships:
        - A one-to-many relationship to Chat (`chats`).
    """

    __tablename__ = "ia_prompts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prompt_name = Column(String(255), nullable=False)
    prompt = Column(Text, nullable=False)
    prompt_description = Column(Text, nullable=True)

    chats = relationship("Chat", back_populates="ia_prompt")


class Model(Base):
    """
    Represents an available AI model.

    This table stores the names of the AI models that can be used to generate
    responses (e.g., 'GPT-4', 'Claude 3').

    Attributes:
        id (UUID): The primary key for the model.
        ia_name (str): The unique name of the AI model.

    Relationships:
        - A one-to-many relationship to Message (`messages`).
    """

    __tablename__ = "models"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ia_name = Column(String(255), nullable=False, unique=True)

    messages = relationship("Message", back_populates="model")


class Message(Base):
    """
    Represents a single message within a chat conversation.

    Each message has an order number to maintain the sequence of the dialogue.
    It can be a user's message or an AI's response.

    Attributes:
        id (UUID): The primary key for the message.
        order_number (int): The sequence number of the message within the chat.
        content (str): The text content of the message.
        statistics (JSON): A field to store structured metadata, such as token counts.
        chat_id (UUID): A foreign key linking to the `chats` table.
        model_id (UUID): A foreign key linking to the `models` table.

    Relationships:
        - A many-to-one relationship to Chat (`chat`).
        - A many-to-one relationship to Model (`model`).
    """

    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_number = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    statistics = Column(JSON)
    chat_id = Column(UUID(as_uuid=True), ForeignKey("chats.id"), nullable=False)
    model_id = Column(UUID(as_uuid=True), ForeignKey("models.id"))

    chat = relationship("Chat", back_populates="messages")
    model = relationship("Model", back_populates="messages")
