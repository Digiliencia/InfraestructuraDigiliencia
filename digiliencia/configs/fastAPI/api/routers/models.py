# /api/routers/models.py
"""
This module defines the API route for retrieving the list of available AI models.

This endpoint is public and does not require user authentication, allowing any
client to discover the models available for use in the system.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import uuid

from db.models import Model
from schemas import chat as chat_schema
from db.session import get_db
from core.endpoints import MODEL_LIST

router = APIRouter()


@router.get(
    MODEL_LIST,
    response_model=chat_schema.Models,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Tuple Available AI Models",
    description="Retrieves a list of all available AI models that can be used in chat conversations. This is a public endpoint and does not require authentication.",
    response_description="A list containing a summary for each available AI model.",
    responses={
        202: {
            "description": "The request was accepted and the list of models is returned.",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "idModel": "68b92fa2-fe59-4181-99a5-032190d68a73",
                            "model_name": "GPT-4",
                        },
                        {
                            "idModel": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                            "model_name": "Claude 3",
                        },
                    ]
                }
            },
        }
    },
)
async def get_models(
    db: AsyncSession = Depends(get_db),
) -> chat_schema.Models:
    """
    Retrieves a list of all configured AI models from the database.

    Args:
        db (AsyncSession): The database session, injected by dependency.

    Returns:
        A tuple where each item is a `ModelSummary` object, containing the
        ID and name of an AI model.
    """
    result = await db.execute(select(Model.id, Model.ia_name))
    models = result.fetchall()

    model_list: tuple[chat_schema.ModelSummary, ...] = tuple(
        chat_schema.ModelSummary(
            idModel=uuid.UUID(str(model.id)), model_name=model.ia_name
        )
        for model in models
    )
    return chat_schema.Models(models=model_list)
