# /schemas/user.py
from pydantic import BaseModel, EmailStr, field_validator


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserRegister(BaseModel):
    email: EmailStr
    password: str

    # NEW: Password validation
    @field_validator("password")
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        # You can add more rules here (e.g., require numbers, symbols, etc.)
        return v


class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
