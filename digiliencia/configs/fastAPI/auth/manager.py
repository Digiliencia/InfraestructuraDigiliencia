# /auth/manager.py
"""
This module provides the core user management logic for the application.

It defines a custom `UserManager` class that extends the functionality of
fastapi-users to handle user creation, password validation with custom
policies, and authentication.
"""

import uuid
from typing import Optional, AsyncGenerator
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users.exceptions import InvalidPasswordException

from .db import get_user_db
from core.config import settings
from db.models import User
from schemas.user import UserRegistration
from schemas.user import UserLogin, UserCreate

SECRET = settings.JWT_SECRET_KEY


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """
    Manages user-related operations, including custom password policies.

    This class inherits from the fastapi-users BaseUserManager and provides
    the business logic for handling users. It specifies the secrets for
    password reset and email verification tokens.
    """

    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def validate_password(self, password: str, user: UserRegistration):
        """
        Validates a password against custom strength policies.

        This method is called during user creation and password changes. It
        first runs the default validation from the parent class and then enforces
        a custom policy:
        - Must be at least 8 characters long.
        - Must contain at least one number.
        - Must contain at least one letter.

        Args:
            password (str): The password to validate.
            user (UserRegistration): The user data object.

        Raises:
            InvalidPasswordException: If the password does not meet the policy.
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

    async def authenticate_json(self, credentials: UserLogin) -> Optional[User]:
        """
        Override the default authenticate method to use email and password.

        Returns the authenticated user or None if authentication fails.
        """
        try:
            user = await self.user_db.get_by_email(credentials.email)
        except Exception:
            return None

        if not user or not user.is_active:
            return None

        verified, updated_password_hash = self.password_helper.verify_and_update(
            credentials.password, user.hashed_password
        )
        if not verified:
            return None

        if updated_password_hash is not None:
            await self.user_db.update(user, {"hashed_password": updated_password_hash})

        return user

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        """
        Hook called after a user has successfully registered.

        Args:
            user (User): The user that has just been created.
            request (Optional[Request]): The original FastAPI request object.
        """
        print(f"User {user.id} has registered.")

    async def create(
        self,
        user_create_public: UserRegistration,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> User:
        """
        Creates a new user, adapting the public registration schema.

        This method overrides the default `create` method to accept the
        simplified `UserRegistration` schema from the public API. It then
        converts this into the internal `UserCreate` schema that the parent
        `create` method expects, setting default values for non-public fields.

        Args:
            user_create_public (UserRegistration): The user data from the public
                                                   registration form.
            safe (bool): If True, sensitive data is not included in the response.
            request (Optional[Request]): The original FastAPI request object.

        Returns:
            User: The newly created user object.
        """
        user_create_internal = UserCreate(
            email=user_create_public.email,
            password=user_create_public.password,
            is_active=True,
            is_superuser=False,
            is_verified=False,
        )

        created_user = await super().create(user_create_internal, safe, request)

        return created_user


async def get_user_manager(
    user_db=Depends(get_user_db),
) -> AsyncGenerator[UserManager, None]:
    """
    FastAPI dependency to get an instance of the UserManager.

    Args:
        user_db: The user database adapter, injected by dependency.

    Yields:
        An instance of the UserManager.
    """
    yield UserManager(user_db)
