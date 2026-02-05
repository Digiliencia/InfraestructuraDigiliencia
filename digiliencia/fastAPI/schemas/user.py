# /schemas/user.py
"""
This module defines the Pydantic schemas for user authentication and management.

It leverages `fastapi-users` base schemas for standard operations and defines
custom schemas for public registration and JSON-based login flows.
"""

import uuid

from fastapi_users import schemas
from pydantic import BaseModel, EmailStr, Field


class UserRead(schemas.BaseUser[uuid.UUID]):
    """
    Public schema for reading user profile data.

    Inherits from `fastapi-users` default schema. It automatically serializes
    the user ID, email, and status flags (is_active, is_superuser), while
    excluding sensitive data like the password hash.
    """

    pass


class UserUpdate(schemas.BaseUserUpdate):
    """
    Schema for updating user profile information.

    Used for the 'PATCH /users/me' endpoint. All fields are optional, allowing
    partial updates.
    """

    pass


class UserCreate(schemas.BaseUserCreate):
    """
    Internal schema for user creation.

    This schema is used by the internal `UserManager` logic. It strictly follows
    the `fastapi-users` requirements for creating a user entry in the database.
    """

    pass


class UserRegistration(BaseModel):
    """
    Public schema for the user sign-up endpoint.

    This represents the data actually sent by the frontend client during registration.

    Attributes:
        email (EmailStr): A valid email address.
        password (str): The plain text password (min length 8).
    """

    email: EmailStr = Field(
        ...,
        title="User Email",
        description="The email address for account registration.",
        examples=["user@example.com"],
    )
    password: str = Field(
        ...,
        title="Password",
        description="The user's password. Must meet complexity requirements.",
        min_length=8,
        examples=["StrongPass123!"],
    )


class UserLogin(BaseModel):
    """
    Schema for JSON-based login credentials.

    Used for the custom '/auth/login' endpoint.

    Attributes:
        email (EmailStr): The registered email address.
        password (str): The user's password.
    """

    email: EmailStr = Field(
        ...,
        title="User Email",
        description="The registered email address.",
        examples=["user@example.com"],
    )
    password: str = Field(
        ...,
        title="Password",
        description="The password associated with the email.",
        examples=["StrongPass123!"],
    )
