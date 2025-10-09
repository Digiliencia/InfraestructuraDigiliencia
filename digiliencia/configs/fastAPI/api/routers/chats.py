# /api/routers/chats.py
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Tuple
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import and_, or_, not_
from sqlalchemy import exc as sqlalchemy_exc
from db.models import Model, User, Chat, Message, IAPrompt
from schemas import chat as chat_schema
from auth.users import fastapi_users
from db.session import get_db
from sqlalchemy.exc import IntegrityError


# Crear una dependencia reutilizable para el usuario actual
current_user = fastapi_users.current_user(active=True)

router = APIRouter(dependencies=[Depends(current_user)])


@router.get(
    "/conversations",
    response_model=chat_schema.ConversationSummaryList,
    summary="List User Conversations",
    description="Retrieve a list of all conversations for the authenticated user",
    response_description="Dictionary of conversations with their IDs and titles",
    responses={
        200: {
            "description": "List of user's conversations",
            "content": {
                "application/json": {
                    "example": {
                        "conversations": {
                            "conversation1": {
                                "idChat": "550e8400-e29b-41d4-a716-446655440000",
                                "Título": "General Questions",
                            },
                            "conversation2": {
                                "idChat": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
                                "Título": "Technical Support",
                            },
                        }
                    }
                }
            },
        },
        401: {
            "description": "Not authenticated",
            "content": {
                "application/json": {"example": {"detail": "Not authenticated"}}
            },
        },
    },
)
async def get_user_chat_list(
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationSummaryList:
    """
    Retrieve a summary for the authenticated user.

    This endpoint returns a list of chat summaries associated with the
    authenticated user, including their IDs and titles. The conversations are
    sorted by their creation date.

    Security:
    - Requires authentication
    - Users can only see their own conversations
    - Active account required

    Parameters:
        user (User): Current authenticated user (injected)
        db (AsyncSession): Database session (injected)

    Returns:
        ConversationSummaryList: Dictionary containing:
            - conversations (dict): Map of conversation IDs to their details
                - idChat (UUID): Unique identifier for the chat
                - tittle (str): Title/name of the conversation
                - ia_prompt (str): IA prompt associated with the conversation

    Example:
        ```json
        {
            "conversations": {
                "conversation1": {
                    "idChat": "550e8400-e29b-41d4-a716-446655440000",
                    "tittle": "General Questions",
                    "ia_prompt": "What is the capital of France?"
                },
                "conversation2": {
                    "idChat": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
                    "tittle": "Technical Support",
                    "ia_prompt": "How do I reset my password?"
                }
            }
        }
        ```
    """
    result = await db.execute(select(Chat).where(Chat.user_id == user.id))
    chats = result.scalars().all()
    summary = [
        chat_schema.ConversationSummary(
            idChat=str(chat.id), tittle=str(chat.tittle), ia_prompt=chat.ia_prompt
        )
        for chat in chats
    ]
    return chat_schema.ConversationSummaryList(conversations=summary)


@router.get("/chats/{chat_id}", response_model=List[chat_schema.Texts])
async def get_full_conversation(
    chat_id: uuid.UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationList:
    """
    Retrieve a full conversation by its ID.

    Parameters:
        chat_id (UUID): The unique identifier of the chat
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        ConversationList: List of messages in the conversation

    Raises:
        HTTPException: If chat is not found or user is not authorized
    """
    chat = await db.get(Chat, chat_id)
    if chat is None or chat.user_id != user.id:
        raise HTTPException(status_code=404, detail="Chat not found")
    result = await db.execute(
        select(Message).where(Message.chat_id == chat_id).order_by(Message.n_orden)
    )
    messages = result.scalars().all()
    conversations = chat_schema.ConversationFull(
        idChat=str(chat.id),
        tittle=str(chat.tittle),
        ia_prompt=chat.ia_prompt,
        messages=[
            chat_schema.message(
                id=str(msg.id),
                order_number=msg.n_orden,
                content=str(msg.content),
                model=msg.model,
            )
            for msg in messages
        ],
    )
    return chat_schema.ConversationList(conversations=[conversations])


@router.patch("/chats/{chat_id}", response_model=chat_schema.Texts)
async def ask_question_to_chat(
    chat_id: uuid.UUID,
    payload: chat_schema.Text,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.Texts:
    """
    Send a question to a specific chat and get an AI-generated response.

    Parameters:
        chat_id (UUID): The unique identifier of the chat
        payload (Text): Contains the question text and model configuration
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        Texts: The AI-generated response

    Raises:contenido
        HTTPException: If chat is not found or user is not authorized
    """
    chat = await db.get(Chat, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    if not chat.user_id.is_(user.id):
        raise HTTPException(
            status_code=403, detail="Not authorized to access this chat"
        )
    # Guardar la pregunta
    n_orden = (
        (await db.execute(select(Message.n_orden).where(Message.chat_id == chat_id)))
        .scalars()
        .all()
    )
    n_orden = max(n_orden) + 1 if n_orden else 1
    message = Message(chat_id=chat_id, order_number=n_orden, content=payload.text)
    db.add(message)
    await db.commit()
    await db.refresh(message)
    # Llamada a servicio externo (placeholder)
    respuesta = (
        f"Respuesta simulada a '{payload.text}' usando el modelo {payload.model}"
    )
    # Guardar la respuesta
    n_orden += 1
    response_message = Message(chat_id=chat_id, order_number=n_orden, content=respuesta)
    db.add(response_message)
    await db.commit()
    await db.refresh(response_message)
    return chat_schema.Texts(text=respuesta)


@router.patch("/chats", response_model=chat_schema.Texts)
async def create_chat(
    payload: chat_schema.ChatCreate,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> chat_schema.ConversationSummary:
    """
    Create a conversation.

    Parameters:
        payload (ChatCreate): Contains the template for the AI prompt and title.
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        chat_id: chat id

    Raises:
        HTTPException: If user is not authorized
    """
    ia_prompt = await db.execute(
        select(IAPrompt).where(IAPrompt.prompt_name == payload.ia_prompt)
    )
    ia_prompt = ia_prompt.scalars().first()
    if not ia_prompt:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid ia_prompt: The specified prompt does not exist",
        )
    chat = Chat(user_id=user.id, ia_prompt=payload.ia_prompt, tittle=payload.tittle)
    db.add(chat)
    await db.commit()
    return chat_schema.ConversationSummary(
        idChat=str(chat.id), tittle=str(chat.tittle), ia_prompt=ia_prompt
    )


@router.put("/chats", response_model=List[chat_schema.Texts])
async def import_conversation(
    payload: List[chat_schema.Texts],
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> tuple[UUID, List[chat_schema.Texts]]:
    """
    Import a full conversation.

    Parameters:
        payload (List[Texts]): List of messages to import into the chat
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        Tuple[UUID, List[Texts]]: The ID of the new chat and the imported messages

    Raises:

    """
    chat = Chat(user_id=user.id, tittle="Imported Chat")
    db.add(chat)
    # Insertar nuevos mensajes
    for i, msg in enumerate(payload, start=1):
        db.add(Message(chat_id=chat.id, order_number=i, content=msg.text))
    await db.commit()
    return UUID(str(chat.id)), payload


@router.delete("/chats/{chat_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_conversation(
    chat_id: UUID,
    user: User = Depends(current_user),
    db: AsyncSession = Depends(get_db),
) -> None:
    """
    Delete a specific chat conversation and all its messages.

    Parameters:
        chat_id (UUID): The unique identifier of the chat to delete
        user (User): Current authenticated user (injected by dependency)
        db (AsyncSession): Database session (injected by dependency)

    Returns:
        None: Returns 204 No Content on success

    Raises:
        HTTPException: If chat is not found or user is not authorized
    """
    chat = await db.get(Chat, chat_id)
    if chat is None or not chat.user_id.is_(user.id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Chat not found"
        )
    await db.delete(chat)
    await db.commit()
    return None


@router.get("/chats/model_list")
async def get_ia_list(db: AsyncSession = Depends(get_db)):
    models = await db.execute(select(Model))
    models = models.fetchall()
    model_list = [{"id": model.id, "model": model.nombre} for model in models]
    return model_list


@router.get("/chats/template_list", status_code=status.HTTP_202_ACCEPTED)
async def get_template_list(db: AsyncSession = Depends(get_db)):
    templates = await db.execute(select(IAPrompt))
    templates = templates.fetchall()
    template_list = [
        {
            "id": template.id,
            "template_name": template.prompt_name,
            "template_description": template.prompt_description,
        }
        for template in templates
    ]
    return template_list
