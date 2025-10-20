# /schemas/user.py
"""
This module defines the Pydantic models (schemas) for user-related operations,
leveraging the base schemas provided by the `fastapi-users` library.

These schemas are used for API request/response validation, data serialization,
and automatic OpenAPI documentation for endpoints related to user registration,
authentication, and management.
"""

import uuid
from fastapi_users import schemas
from pydantic import BaseModel, EmailStr


class UserRead(schemas.BaseUser[uuid.UUID]):
    """
    Schema for reading user data.

    This model represents the public-facing view of a user object. It inherits
    from the `fastapi-users` base schema and automatically includes fields like
    `id`, `email`, `is_active`, etc., while omitting sensitive data like
    `hashed_password`. It is used as the response model for endpoints that
    return user information.
    """

    pass


class UserUpdate(schemas.BaseUserUpdate):
    """
    Schema for updating an existing user's data.

    This model is used as the request body for endpoints that allow a user
    to update their own profile information. It inherits from the `fastapi-users`
    base update schema, which makes all fields optional.
    """

    pass


class UserCreate(schemas.BaseUserCreate):
    """
    Internal schema for creating a new user.

    This model includes all required fields for creating a user record in the
    database, as expected by the internal logic of `fastapi-users`. It is
    distinct from the public-facing registration schema.
    """

    pass


class UserRegistration(BaseModel):
    """
    Schema for the public user registration endpoint.

    This model defines the fields a new user must provide when signing up.
    It serves as the request body for the `/register` endpoint.

    Attributes:
        email (EmailStr): The user's email address. It is validated to ensure
                          it has a correct email format.
        password (str): The user's desired password. Further validation
                        (e.g., for strength) is handled by the user manager.
    """

    email: EmailStr
    password: str


class UserLogin(BaseModel):
    """
    Schema for the user login endpoint.

    This model defines the credentials required for a user to authenticate.
    It is used as the request body for the `/auth/login` endpoint.

    Attributes:
        email (EmailStr): The user's registered email address.
        password (str): The user's password.
    """

    email: EmailStr
    password: str
