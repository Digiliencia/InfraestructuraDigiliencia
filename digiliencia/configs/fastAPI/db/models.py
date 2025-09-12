# /db/models.py
import uuid
from sqlalchemy import Column, Integer, String, Text, ForeignKey, JSON, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from .session import Base

chat_iaprompt_association = Table(
    "chat_iaprompt_association",
    Base.metadata,
    Column("chat_id", UUID(as_uuid=True), ForeignKey("chats.id"), primary_key=True),
    Column(
        "iaprompt_id", UUID(as_uuid=True), ForeignKey("ia_prompts.id"), primary_key=True
    ),
)


class User(SQLAlchemyBaseUserTableUUID, Base):
    # fastapi-users already provides:
    # id (UUID), email, hashed_password, is_active, is_superuser, is_verified
    __tablename__ = "users"
    chats = relationship("Chat", back_populates="owner", cascade="all, delete-orphan")


class Chat(Base):
    __tablename__ = "chats"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    titulo = Column(String(255), index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="chats")
    messages = relationship(
        "Message", back_populates="chat", cascade="all, delete-orphan"
    )
    prompts = relationship(
        "IAPrompt", secondary=chat_iaprompt_association, back_populates="chats"
    )


class IAPrompt(Base):
    __tablename__ = "ia_prompts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(255), nullable=False, unique=True)
    descripcion = Column(Text)
    prompt = Column(Text, nullable=False)

    chats = relationship(
        "Chat", secondary=chat_iaprompt_association, back_populates="prompts"
    )


class Model(Base):
    __tablename__ = "models"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(255), nullable=False, unique=True)

    messages = relationship("Message", back_populates="model")


class Message(Base):
    __tablename__ = "messages"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    n_orden = Column("Order_number", Integer, nullable=False)
    contenido = Column(Text, nullable=False)
    estadisticas = Column("Statistics", JSON)

    chat_id = Column(UUID(as_uuid=True), ForeignKey("chats.id"), nullable=False)
    modelo_id = Column(UUID(as_uuid=True), ForeignKey("models.id"))

    chat = relationship("Chat", back_populates="messages")
    model = relationship("Model", back_populates="messages")
