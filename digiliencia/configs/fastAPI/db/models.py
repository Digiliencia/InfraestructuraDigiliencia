# /db/models.py
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
from fastapi_users.db import SQLAlchemyBaseUserTableUUID

# Define a Base for declarative models
Base = declarative_base()


class User(SQLAlchemyBaseUserTableUUID, Base):
    """
    User model based on FastAPI Users, linked to chats.
    """

    __tablename__ = "users"

    # fastapi-users provides: id, email, hashed_password, is_active, is_superuser, is_verified

    # Relationship to Chat: one user can have many chats
    chats = relationship("Chat", back_populates="owner", cascade="all, delete-orphan")


class Chat(Base):
    """
    Chat model, representing a single conversation.
    """

    __tablename__ = "chats"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tittle = Column(String(255), index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    ia_prompt_id = Column(UUID(as_uuid=True), ForeignKey("ia_prompts.id"))

    # Relationship back to User
    owner = relationship("User", back_populates="chats")
    # Relationship to Message: one chat can have many messages
    messages = relationship(
        "Message", back_populates="chat", cascade="all, delete-orphan"
    )
    ia_prompt = relationship("IAPrompt", back_populates="chats")


class IAPrompt(Base):
    """
    IA_Prompt model, representing a system prompt template for the AI.
    """

    __tablename__ = "ia_prompts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prompt_name = Column(String(255), nullable=False)
    prompt = Column(Text, nullable=False)
    prompt_description = Column(Text, nullable=True)
    ia_name = Column(String(255), nullable=False, unique=True)

    # Relationship to Chat: one prompt can be used in many chats
    chats = relationship("Chat", back_populates="ia_prompt")


class Model(Base):
    """
    Model class, representing an available AI model (e.g., 'GPT-4').
    """

    __tablename__ = "models"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ia_name = Column(String(255), nullable=False, unique=True)

    # Relationship to Message: one model can be used in many messages
    messages = relationship("Message", back_populates="model")


class Message(Base):
    """
    Message model, representing a single message within a chat.
    """

    __tablename__ = "messages"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_number = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    statistics = Column(JSON)  # Using JSON type is better for structured data

    # Foreign Keys
    chat_id = Column(UUID(as_uuid=True), ForeignKey("chats.id"), nullable=False)
    model_id = Column(UUID(as_uuid=True), ForeignKey("models.id"))

    # Relationships back to parent tables
    chat = relationship("Chat", back_populates="messages")
    model = relationship("Model", back_populates="messages")
