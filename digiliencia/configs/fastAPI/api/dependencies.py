from fastapi import Request
from db.models import User


async def get_current_user(request: Request) -> User:
    """Get the current user from the request state"""
    return request.state.user
