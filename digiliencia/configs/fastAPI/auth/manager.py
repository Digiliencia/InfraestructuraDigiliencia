# /auth/manager.py
import uuid
from typing import Optional, AsyncGenerator
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.exceptions import InvalidPasswordException
from fastapi_users.password import PasswordHelper

from .db import get_user_db
from core.config import settings
from db.models import User
from schemas.user import UserRegistration


SECRET = settings.JWT_SECRET_KEY

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """
    Manages user-related operations like password hashing and validation.
    """
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def validate_password(self, password: str, user: UserRegistration):
        """
        Validates a password against the user model.
        This is the recommended place to add password strength logic.
        """
        # default validation
        await super().validate_password(password, user)
        
        # Custom password policy
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="La contraseña debe tener al menos 8 caracteres."
            )
        if not any(char.isdigit() for char in password):
            raise InvalidPasswordException(
                reason="La contraseña debe contener al menos un número."
            )
        if not any(char.isalpha() for char in password):
            raise InvalidPasswordException(
                reason="La contraseña debe contener al menos una letra."
            )


async def get_user_manager(user_db = Depends(get_user_db)) -> AsyncGenerator[UserManager, None]:
    """
    Dependency that provides the user manager instance.
    """
    yield UserManager(user_db)