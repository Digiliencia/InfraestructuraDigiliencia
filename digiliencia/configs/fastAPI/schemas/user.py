# /schemas/user.py
import uuid
from fastapi_users import schemas
from pydantic import BaseModel, EmailStr


class UserRead(schemas.BaseUser[uuid.UUID]):
    """Schema for reading user data."""

    pass


class UserUpdate(schemas.BaseUserUpdate):
    """Schema for updating user data."""

    pass

class UserCreate(schemas.BaseUserCreate):
    """
    Internal schema for creating a user. Includes all required fields
    with their default values for fastapi-users logic.
    """
    pass

class UserRegistration(BaseModel):
    """
    Schema for the public registration endpoint.
    Only asks for the required fields from the user.
    """

    email: EmailStr
    password: str

class UserLogin(BaseModel):
    """
    Schema used for user login with email and password.
    """
    email: EmailStr
    password: str