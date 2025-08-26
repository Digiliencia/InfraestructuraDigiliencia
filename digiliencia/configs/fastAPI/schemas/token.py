# /schemas/token.py
from pydantic import BaseModel


# Token response includes both tokens
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    email: str | None = None


# Schema for the refresh token request
class RefreshTokenRequest(BaseModel):
    refresh_token: str
