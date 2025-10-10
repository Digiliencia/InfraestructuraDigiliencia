# /api/routers/templates.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import IAPrompt
from schemas import chat as chat_schema
from db.session import get_db

router = APIRouter()


@router.get("/chats/template_list", status_code=status.HTTP_202_ACCEPTED)
async def get_template_list(
    db: AsyncSession = Depends(get_db),
) -> tuple[chat_schema.TemplateSummary, ...]:
    templates = await db.execute(
        select(IAPrompt.id, IAPrompt.prompt_name, IAPrompt.prompt_description)
    )
    templates = templates.fetchall()
    template_list = tuple(
        chat_schema.TemplateSummary(
            idTemplate=str(template.id),
            template_name=template.prompt_name,
            template_description=template.prompt_description,
        )
        for template in templates
    )
    return template_list
