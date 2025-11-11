# /api/routers/custom_users.py
"""
This module defines custom API routes for user account management.

It provides endpoints for authenticated users to retrieve, update, and delete
their own account information. These endpoints are protected and require a valid
JWT access token for authorization.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from auth.manager import get_user_manager, UserManager
from schemas.user import UserRead, UserUpdate
from db.models import User
from auth.users import fastapi_users
from core.endpoints import USERS_ME

# Reusable dependency for the currently authenticated, active user.
current_user = fastapi_users.current_user(active=True)

router = APIRouter()


@router.get(
    USERS_ME,
    response_model=UserRead,
    summary="Get Current User Data",
    description="Retrieve the profile information for the currently authenticated user.",
    response_description="The authenticated user's profile data.",
    responses={
        200: {"description": "Successful retrieval of user data."},
        401: {"description": "User is not authenticated."},
    },
)
async def get_my_data(
    user: User = Depends(current_user),
):
    """
    Retrieves the data for the currently authenticated user.

    Args:
        user (User): The authenticated user object, injected by the
                     `current_user` dependency.

    Returns:
        User: The user object, which will be serialized according to the
              `UserRead` Pydantic model.
    """
    return user


@router.patch(
    USERS_ME,
    response_model=UserRead,
    summary="Update Current User Data",
    description="Update the profile information for the currently authenticated user. Note: Password updates should be handled via a dedicated password change endpoint.",
    response_description="The updated user's profile data.",
    responses={
        200: {"description": "User data was successfully updated."},
        400: {
            "description": "The update payload is invalid (e.g., email already exists)."
        },
        401: {"description": "User is not authenticated."},
    },
)
async def update_my_data(
    payload: UserUpdate,
    user: User = Depends(current_user),
    user_manager: UserManager = Depends(get_user_manager),
):
    """
    Updates the data for the currently authenticated user.

    Args:
        payload (UserUpdate): The request body containing the user data to update.
        user (User): The authenticated user object to be updated.
        user_manager (UserManager): The user management service, injected by dependency.

    Returns:
        User: The updated user object, serialized by the `UserRead` model.

    Raises:
        HTTPException: 400 Bad Request if the update fails (e.g., due to a
                       duplicate email).
    """
    try:
        user = await user_manager.update(
            payload, user, safe=True
        )  # safe=True prevents password updates
        return user
    except Exception as e:
        # Catch potential exceptions from the user manager, like email conflicts.
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.delete(
    USERS_ME,
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete Current User Account",
    description="Permanently delete the account of the currently authenticated user.",
    response_description="No content is returned on successful deletion.",
    responses={
        204: {"description": "The user account was successfully deleted."},
        401: {"description": "User is not authenticated."},
    },
)
async def delete_my_data(
    user: User = Depends(current_user),
    user_manager: UserManager = Depends(get_user_manager),
):
    """
    Deletes the account of the currently authenticated user.

    Args:
        user (User): The authenticated user object to be deleted.
        user_manager (UserManager): The user management service, injected by dependency.

    Returns:
        None
    """
    await user_manager.delete(user)
    return None


@router.post(
    USERS_ME,
    summary="Logout User",
    description="Logs out the currently authenticated user.",
    response_description="Logout successful message",
    responses={
        200: {
            "description": "Successful logout",
            "content": {
                "application/json": {"example": {"detail": "Logout successful"}}
            },
        },
        401: {
            "description": "User not authenticated",
            "content": {
                "application/json": {"example": {"detail": "Not authenticated"}}
            },
        },
    },
)
async def logout(
    user: User = Depends(current_user),
):
    """
    Logs out the current user.

    This endpoint requires a valid Bearer token in the Authorization header.
    For stateless JWT (Bearer) authentication, this endpoint serves as
    a server-side confirmation. The client is responsible for deleting/discarding
    the token locally.

    Parameters:
        user (User): The currently authenticated user (injected).

    Returns:
        dict: A confirmation message.

    Raises:
        HTTPException:
            - 401: If no valid token is provided or the user is inactive.
    """
    # For stateless Bearer tokens, logout is a "no-op" on the server.
    # The client is responsible for discarding the token.
    # We just return a success message to confirm authentication.
    return {"detail": "Logout successful"}
