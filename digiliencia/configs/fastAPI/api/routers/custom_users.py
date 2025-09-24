# /api/routers/custom_users.py
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from main import fastapi_users

from db.models import User

router = APIRouter()


@router.delete(
    "/users/me",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Own Account",
    description="Permanently delete the authenticated user's account",
    responses={
        204: {"description": "Account successfully deleted"},
        401: {
            "description": "Not authenticated",
            "content": {
                "application/json": {"example": {"detail": "Not authenticated"}}
            },
        },
        403: {
            "description": "Token expired",
            "content": {
                "application/json": {"example": {"detail": "Token has expired"}}
            },
        },
    },
)
async def delete_own_user(
    user: User = Depends(fastapi_users.current_user(active=True)),
    user_manager=Depends(fastapi_users.get_user_manager),
):
    """
    Permanently delete the authenticated user's account.

    This endpoint allows users to delete their own account. This action is irreversible
    and will delete all associated data including chats and preferences.

    Security:
    - Requires authentication
    - Can only delete own account
    - Active account required

    Parameters:
        user (User): Current authenticated user (injected)
        user_manager: User management service (injected)

    Returns:
        None: Returns 204 No Content on successful deletion

    Raises:
        HTTPException:
            - 401: Not authenticated
            - 403: Token expired

    Note:
        This operation cannot be undone. All user data will be permanently deleted.
    """
    await user_manager.delete(user)
    return None


@router.get(
    "/users/{user_id}/export",
    summary="Export User Data",
    description="Export all data associated with a user account (GDPR compliance)",
    response_description="User's personal data and usage statistics",
    responses={
        200: {
            "description": "User data successfully exported",
            "content": {
                "application/json": {
                    "example": {
                        "id": "550e8400-e29b-41d4-a716-446655440000",
                        "email": "user@example.com",
                        "is_active": True,
                        "chats_count": 5,
                    }
                }
            },
        },
        403: {
            "description": "Not authorized to access this data",
            "content": {"application/json": {"example": {"detail": "Not authorized"}}},
        },
        404: {
            "description": "User not found",
            "content": {"application/json": {"example": {"detail": "User not found"}}},
        },
    },
)
async def export_user_data(
    user_id: uuid.UUID,
    current_user: User = Depends(fastapi_users.current_user(active=True)),
):
    """
    Export all data associated with a user account (GDPR compliance).

    This endpoint allows users to export all their personal data stored in the system,
    including account details and usage statistics. Users can only export their own data.

    Security:
    - Requires authentication
    - Users can only export their own data
    - Active account required

    Parameters:
        user_id (UUID): The ID of the user whose data is being exported
        current_user (User): Current authenticated user (injected)

    Returns:
        dict: User's data including:
            - id (UUID): User's unique identifier
            - email (str): User's email address
            - is_active (bool): Account status
            - chats_count (int): Number of chat conversations

    Raises:
        HTTPException:
            - 403: Attempting to access another user's data
            - 404: User not found

    Example:
        ```json
        {
            "id": "550e8400-e29b-41d4-a716-446655440000",
            "email": "user@example.com",
            "is_active": true,
            "chats_count": 5
        }
        ```

    Note:
        This endpoint is provided for GDPR compliance, allowing users
        to access all their personal data stored in the system.
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
