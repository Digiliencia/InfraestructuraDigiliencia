# /api/routers/models.py
"""
This module defines the API routes for retrieving available AI models.

It exposes a public endpoint that allows clients to discover which AI models
are currently supported and configured in the system for chat interactions.
"""

import uuid
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.endpoints import MODEL_LIST
from db.models import Model
from db.session import get_db
from schemas import chat as chat_schema

router = APIRouter()


@router.get(
    MODEL_LIST,
    response_model=chat_schema.Models,
    status_code=status.HTTP_200_OK,
    summary="List Available AI Models",
    description="Retrieves a list of all available AI models configured for chat conversations. This is a public endpoint.",
    response_description="A collection of model summaries.",
    responses={
        200: {
            "description": "Successfully retrieved the list of models.",
            "content": {
                "application/json": {
                    "example": {
                        "models": [
                            {
                                "id": "68b92fa2-fe59-4181-99a5-032190d68a73",
                                "name": "GPT-4",
                            },
                            {
                                "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
                                "name": "Claude 3",
                            },
                        ]
                    }
                }
            },
        }
    },
)
async def get_models(
    db: AsyncSession = Depends(get_db),
) -> chat_schema.Models:
    """
    Fetches all configured AI models from the database.

    Args:
        db (AsyncSession): The database session dependency.

    Returns:
        chat_schema.Models: An object containing a list/tuple of model summaries.
    """
    query = select(Model.id, Model.name)

    result = await db.execute(query)
    models_data = result.fetchall()

    # Transform DB result into the Pydantic schema
    model_list = tuple(
        chat_schema.ModelSummary(
            id=uuid.UUID(str(row.id)),
            name=str(row.name),
        )
        for row in models_data
    )

    return chat_schema.Models(models=model_list)
