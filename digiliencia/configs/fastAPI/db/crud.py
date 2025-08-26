# /db/crud.py
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from . import models
from schemas import user as user_schema
from core.security import get_password_hash


async def get_user_by_email(db: AsyncSession, email: str):
    """Fetches a user by email asynchronously."""
    result = await db.execute(select(models.User).filter(models.User.email == email))
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, user: user_schema.UserRegister):
    """Creates a new user asynchronously."""
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, password=hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user
