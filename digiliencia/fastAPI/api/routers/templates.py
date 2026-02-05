# /api/routers/templates.py
"""
This module defines the API routes for retrieving available AI prompt templates.

It exposes endpoints that allow clients to discover predefined
"personas" or templates (e.g., "General Assistant", "Code Helper") used to
initialize chat conversations.
"""

import uuid
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.endpoints import TEMPLATE_LIST, TEMPLATE_DETAIL
from db.models import AIPrompt
from db.session import get_db
from schemas import chat as chat_schema

router = APIRouter()


@router.get(
    TEMPLATE_LIST,
    response_model=chat_schema.Templates,
    status_code=status.HTTP_200_OK,
    summary="List Available Chat Templates",
    description="Retrieves a list of all available AI prompt templates configured in the system.",
    response_description="A collection of template summaries.",
    responses={
        200: {
            "description": "Successfully retrieved the list of templates.",
            "content": {
                "application/json": {
                    "example": {
                        "templates": [
                            {
                                "id": "76f81605-08ac-4694-8122-18f6958c8797",
                                "name": "General Assistant",
                                "description": "A helpful assistant for general questions.",
                            }
                        ]
                    }
                }
            },
        }
    },
)
async def get_template_list(
    db: AsyncSession = Depends(get_db),
) -> chat_schema.Templates:
    """
    Fetches all configured AI prompt templates from the database.

    Args:
        db (AsyncSession): The database session dependency.

    Returns:
        chat_schema.Templates: An object containing a tuple of template summaries.
    """
    query = select(AIPrompt.id, AIPrompt.name, AIPrompt.description)

    result = await db.execute(query)
    rows = result.fetchall()

    template_list = tuple(
        chat_schema.TemplateSummary(
            id=uuid.UUID(str(row.id)),
            name=str(row.name),
            description=str(row.description),
        )
        for row in rows
    )

    return chat_schema.Templates(templates=template_list)


@router.get(
    TEMPLATE_DETAIL,
    response_model=chat_schema.TemplateSummary,
    status_code=status.HTTP_200_OK,
    summary="Get AI Prompt Template by ID",
    description="Retrieves information about a specific AI prompt template by its ID.",
    response_description="The requested template information.",
    responses={
        200: {
            "description": "Successfully retrieved the template.",
            "content": {
                "application/json": {
                    "example": {
                        "id": "76f81605-08ac-4694-8122-18f6958c8797",
                        "name": "General Assistant",
                        "description": "A helpful assistant for general questions.",
                    }
                }
            },
        },
        404: {
            "description": "Template not found.",
        },
    },
)
async def get_template(
    template_id: uuid.UUID,
    db: AsyncSession = Depends(get_db),
) -> chat_schema.TemplateSummary:
    """
    Fetches a specific AI prompt template by its ID from the database.

    Args:
        template_id (uuid.UUID): The UUID of the template to retrieve.
        db (AsyncSession): The database session dependency.

    Returns:
        chat_schema.TemplateSummary: The template information.

    Raises:
        HTTPException: 404 if template is not found.
    """
    query = select(AIPrompt.id, AIPrompt.name, AIPrompt.description).where(
        AIPrompt.id == template_id
    )

    result = await db.execute(query)
    row = result.first()

    if not row:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Template with ID {template_id} not found.",
        )

    return chat_schema.TemplateSummary(
        id=uuid.UUID(str(row.id)),
        name=str(row.name),
        description=str(row.description) if row.description else "",
    )
