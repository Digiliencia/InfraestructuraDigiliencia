# /auth/db.py
"""
This module provides the database adapter for the fastapi-users library.

It defines a dependency that bridges the application's SQLAlchemy session
with the data access layer required by fastapi-users to perform database
operations on the User model.
"""

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
    FastAPI dependency that provides a user database adapter.

    This function is used as a dependency in other parts of the authentication
    system (like the user manager) to get a database interface that is
    compatible with fastapi-users. It wraps the standard SQLAlchemy session
    in the `SQLAlchemyUserDatabase` class.

    Args:
        session (AsyncSession): The asynchronous SQLAlchemy session, injected
                                by the `get_db` dependency.

    Yields:
        SQLAlchemyUserDatabase: An instance of the database adapter configured
                                with the current session and the User model.
    """
    yield SQLAlchemyUserDatabase(session, User)
