# /schemas/user.py
import uuid
from fastapi_users import schemas
from pydantic import BaseModel, EmailStr, field_validator


class UserRead(schemas.BaseUser[uuid.UUID]):
    """Schema for reading user data."""
    pass

class UserUpdate(schemas.BaseUserUpdate):
    """Schema for updating user data."""
    pass

class UserRegistration(BaseModel):
    """
    Schema used ONLY for user registration.
    It only requires the essential fields.
    """
    email: EmailStr
    password: str
    