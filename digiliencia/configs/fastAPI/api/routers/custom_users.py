# /api/routers/custom_users.py
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from main import fastapi_users

from db.models import User

router = APIRouter()


@router.delete("/users/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_own_user(
    user: User = Depends(fastapi_users.current_user(active=True)),
    user_manager=Depends(fastapi_users.get_user_manager),
):
    """
    Deletes the currently authenticated user.
    """
    await user_manager.delete(user)
    return None


@router.get("/users/{user_id}/export")
async def export_user_data(
    user_id: uuid.UUID,
    current_user: User = Depends(fastapi_users.current_user(active=True)),
):
    """
    Exports all data for a given user. Only accessible by the user themselves.
    """
    if user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized"
        )

    return {
        "id": current_user.id,
        "email": current_user.email,
        "is_active": current_user.is_active,
        "chats_count": len(current_user.chats) if current_user.chats else 0,
    }
