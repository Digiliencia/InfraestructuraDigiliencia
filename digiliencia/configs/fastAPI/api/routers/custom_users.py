# /api/routers/custom_users.py
"""
This module defines custom API routes for user account management.

It provides endpoints for authenticated users to retrieve, update, and delete
their own account information. These endpoints are protected and require a valid
JWT access token for authorization.
"""

from typing import Dict

from fastapi import APIRouter, Depends, HTTPException, status
from auth.manager import get_user_manager, UserManager
from schemas.user import UserRead, UserUpdate
from db.models import User
from auth.users import fastapi_users
from core.endpoints import USERS_ME
from fastapi_users import exceptions as fastapi_users_exceptions

# Reusable dependency for the currently authenticated, active user.
current_user = fastapi_users.current_user(active=True)

router = APIRouter()


@router.get(
    USERS_ME,
    response_model=UserRead,
    summary="Get Current User Profile",
    description="Retrieves the profile information for the currently authenticated user.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "User profile retrieved successfully."},
        401: {"description": "User is not authenticated."},
    },
)
async def get_my_data(
    user: User = Depends(current_user),
) -> UserRead:
    """
    Retrieves the data for the currently authenticated user.

    Args:
        user (User): The authenticated user object, injected by the
                     `current_user` dependency.

    Returns:
        UserRead: The serialized user profile object.
    """
    return user


@router.patch(
    USERS_ME,
    response_model=UserRead,
    summary="Update Current User Profile",
    description=(
        "Updates the profile information for the currently authenticated user. "
        "Sensitive fields like passwords cannot be updated here."
    ),
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "User profile updated successfully."},
        400: {"description": "Invalid data (e.g., email already in use)."},
        401: {"description": "User is not authenticated."},
    },
)
async def update_my_data(
    payload: UserUpdate,
    user: User = Depends(current_user),
    user_manager: UserManager = Depends(get_user_manager),
) -> UserRead:
    """
    Updates the data for the currently authenticated user.

    This endpoint uses `safe=True` internally, ensuring that sensitive fields
    (like `is_superuser` or `password`) are ignored even if included in the payload.

    Args:
        payload (UserUpdate): The request body containing the fields to update.
        user (User): The authenticated user object.
        user_manager (UserManager): The user management service.

    Returns:
        UserRead: The updated user profile.

    Raises:
        HTTPException(400): If the email is already associated with another account.
    """
    try:
        # safe=True prevents password and boolean status updates (is_active, etc.)
        updated_user = await user_manager.update(payload, user, safe=True)
        return updated_user
    except fastapi_users_exceptions.UserAlreadyExists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists.",
        )
    except fastapi_users_exceptions.InvalidPasswordException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete(
    USERS_ME,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Current User Account",
    description="Permanently deletes the authenticated user's account.",
    responses={
        204: {"description": "Account deleted successfully."},
        401: {"description": "User is not authenticated."},
    },
)
async def delete_my_data(
    user: User = Depends(current_user),
    user_manager: UserManager = Depends(get_user_manager),
) -> None:
    """
    Deletes the account of the currently authenticated user.

    Args:
        user (User): The authenticated user object.
        user_manager (UserManager): The user management service.
    """
    await user_manager.delete(user)
    return None


@router.post(
    USERS_ME,  # TODO: Consider changing this path to something like '/logout'
    summary="Logout User",
    description="Logs out the currently authenticated user (client-side token discard instruction).",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Logout successful.",
            "content": {
                "application/json": {"example": {"detail": "Logout successful"}}
            },
        },
        401: {"description": "User is not authenticated."},
    },
)
async def logout(
    user: User = Depends(current_user),
) -> Dict[str, str]:
    """
    Performs a logical logout for the current user.

    For stateless JWT authentication (Bearer tokens), the server does not track
    sessions. This endpoint serves as a confirmation for the client to discard
    the token locally.

    Args:
        user (User): The currently authenticated user (verifies token validity).

    Returns:
        Dict[str, str]: A success message.
    """
    return {"detail": "Logout successful"}
