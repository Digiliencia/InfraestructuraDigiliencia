# /api/routers/models.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Model
from schemas import chat as chat_schema
from db.session import get_db

router = APIRouter()


@router.get("/chats/model_list", status_code=status.HTTP_202_ACCEPTED)
async def get_ia_list(
    db: AsyncSession = Depends(get_db),
) -> tuple[chat_schema.ModelSummary, ...]:
    models = await db.execute(select(Model.id, Model.ia_name))
    models = models.fetchall()
    model_list = tuple(
        chat_schema.ModelSummary(idModel=str(model.id), model_name=model.ia_name)
        for model in models
    )
    return model_list
