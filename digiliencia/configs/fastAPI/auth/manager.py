# /auth/manager.py
"""
This module provides the core user management logic for the application.

It defines a custom `UserManager` class that extends the functionality of
fastapi-users to handle user creation, lifecycle hooks, custom password
validation policies, and authentication logic.
"""

import logging
import uuid
from typing import AsyncGenerator, Optional, Union

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from fastapi_users import exceptions as users_exceptions

from auth.db import get_user_db
from core.config import settings
from db.models import User
from schemas.user import UserCreate, UserLogin, UserRegistration

# Initialize logger for this module
logger = logging.getLogger(__name__)

SECRET = settings.JWT_SECRET_KEY


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    """
    Manages user-related operations, including authentication and registration.

    This class customizes the default `fastapi-users` manager to enforce
    specific password policies and handle JSON-based login flows.
    """

    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def validate_password(
        self, password: str, user: Union[UserCreate, UserRegistration]
    ) -> None:
        """
        Validates a password against custom strength policies.

        Enforces the following rules:
        - Minimum length of 8 characters.
        - Must contain at least one digit.
        - Must contain at least one letter.

        Args:
            password (str): The password to validate.
            user (Union[UserCreate, UserRegistration]): The user data object.

        Raises:
            InvalidPasswordException: If the password does not meet the criteria.
        """
        # Run the default validation (e.g., checking against the password content if needed)
        await super().validate_password(password, user)

        # Custom Password Policy
        if len(password) < 8:
            raise users_exceptions.InvalidPasswordException(
                reason="Password must be at least 8 characters long."
            )
        if not any(char.isdigit() for char in password):
            raise users_exceptions.InvalidPasswordException(
                reason="Password must contain at least one number."
            )
        if not any(char.isalpha() for char in password):
            raise users_exceptions.InvalidPasswordException(
                reason="Password must contain at least one letter."
            )

    async def authenticate_json(self, credentials: UserLogin) -> Optional[User]:
        """
        Authenticates a user using a JSON payload (Email/Password).

        This method manually reproduces the authentication logic usually handled
        by `authenticate()` for OAuth2 forms, but adapted for JSON bodies.

        Args:
            credentials (UserLogin): The user's login credentials.

        Returns:
            Optional[User]: The authenticated user if successful, None otherwise.
        """
        try:
            user = await self.user_db.get_by_email(credentials.email)
        except Exception as e:
            # Log the error for debugging, but don't expose it to the user
            logger.error(f"Error fetching user during authentication: {e}")
            return None

        if not user:
            return None

        if not user.is_active:
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
        Hook triggered after a successful user registration.

        Args:
            user (User): The newly registered user.
            request (Optional[Request]): The request context.
        """
        logger.info(f"New user registered: {user.id} ({user.email})")

    async def create(
        self,
        user_create_public: UserRegistration,
        safe: bool = False,
        request: Optional[Request] = None,
    ) -> User:
        """
        Creates a new user by mapping the public registration schema to the internal model.

        This ensures that sensitive fields (like `is_superuser`) cannot be set
        via the public API, as we strictly define the `UserCreate` internal object.

        Args:
            user_create_public (UserRegistration): Data from the public sign-up form.
            safe (bool): If True, returns a sanitized user object.
            request (Optional[Request]): The request context.

        Returns:
            User: The newly created user.
        """
        # Explicitly map public registration data to internal creation schema
        # to force default values for secure fields.
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
    Dependency that yields a UserManager instance.

    Args:
        user_db: The user database adapter.
    """
    yield UserManager(user_db)
