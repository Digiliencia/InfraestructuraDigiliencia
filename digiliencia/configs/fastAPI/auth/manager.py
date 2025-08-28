# /auth/manager.py
import uuid
from typing import Optional, AsyncGenerator
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from .db import get_user_db
from core.config import settings
from db.models import User

SECRET = settings.JWT_SECRET_KEY

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """
    Manages user-related operations like password hashing and validation.
    """
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

async def get_user_manager(user_db = Depends(get_user_db)) -> AsyncGenerator[UserManager, None]:
    """
    Dependency that provides the user manager instance.
    """
    yield UserManager(user_db)