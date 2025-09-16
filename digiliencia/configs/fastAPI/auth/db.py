# /auth/db.py
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import User
from db.session import get_db


async def get_user_db(
    session: AsyncSession = Depends(get_db),
) -> AsyncGenerator[SQLAlchemyUserDatabase, None]:
    """
    Dependency that provides a user database adapter for FastAPI-Users.
    """
    yield SQLAlchemyUserDatabase(session, User)
