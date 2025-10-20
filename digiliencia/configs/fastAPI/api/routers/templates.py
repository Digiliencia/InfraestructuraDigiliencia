# /api/routers/templates.py
"""
This module defines the API route for retrieving the list of available
AI prompts, also referred to as templates.

This endpoint is public and does not require user authentication, allowing any
client to discover the predefined templates for initiating chat conversations.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from db.models import IAPrompt
from schemas import chat as chat_schema
from db.session import get_db

router = APIRouter()


@router.get(
    "/chats/template_list",
    response_model=tuple[chat_schema.TemplateSummary, ...],
    status_code=status.HTTP_202_ACCEPTED,
    summary="List Available Chat Templates",
    description="Retrieves a list of all available AI prompt templates that can be used to start new chat conversations. This is a public endpoint.",
    response_description="A list containing a summary for each available template.",
    responses={
        202: {
            "description": "The request was accepted and the list of templates is returned.",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "idTemplate": "76f81605-08ac-4694-8122-18f6958c8797",
                            "template_name": "General Assistant",
                            "template_description": "A helpful assistant for general questions.",
                        },
                        {
                            "idTemplate": "a2f4c0c4-7e8d-4a1a-9f2d-8b6c5e0d1b3a",
                            "template_name": "Code Helper",
                            "template_description": "An assistant specialized in programming queries.",
                        },
                    ]
                }
            },
        }
    },
)
async def get_template_list(
    db: AsyncSession = Depends(get_db),
) -> tuple[chat_schema.TemplateSummary, ...]:
    """
    Retrieves a list of all configured AI prompt templates from the database.

    Args:
        db (AsyncSession): The database session, injected by dependency.

    Returns:
        A tuple where each item is a `TemplateSummary` object, containing the
        ID, name, and description of a template.
    """
    result = await db.execute(
        select(IAPrompt.id, IAPrompt.prompt_name, IAPrompt.prompt_description)
    )
    templates = result.fetchall()

    template_list = tuple(
        chat_schema.TemplateSummary(
            idTemplate=str(template.id),
            template_name=template.prompt_name,
            template_description=template.prompt_description,
        )
        for template in templates
    )
    return template_list
