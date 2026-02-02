# /api/routers/custom_auth.py
"""
This module handles custom authentication routes.

It allows users to authenticate using a JSON payload (Email/Password) instead of
the standard OAuth2 form data, facilitating integration with Single Page Applications (SPAs)
and mobile clients.
"""

from fastapi import APIRouter, Depends, HTTPException, Response, status
from auth.manager import get_user_manager, UserManager
from schemas.user import UserLogin
from auth.transport import auth_backend
from core.endpoints import LOGIN

router = APIRouter()


@router.post(
    LOGIN,
    summary="User Login (JSON)",
    description="Authenticates a user via email and password, returning a JWT access token.",
    response_description="JSON response containing the access token and token type.",
    status_code=status.HTTP_200_OK,
    responses={
        200: {
            "description": "Login successful.",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                        "token_type": "bearer",
                    }
                }
            },
        },
        400: {"description": "Bad Request (Invalid credentials format)."},
        401: {
            "description": "Authentication failed (Invalid email, password, or inactive user).",
            "content": {
                "application/json": {
                    "example": {"detail": "Incorrect email or password"}
                }
            },
        },
    },
)
async def login_with_json(
    credentials: UserLogin,
    user_manager: UserManager = Depends(get_user_manager),
) -> Response:
    """
    Authenticates a user and issues an access token.

    This endpoint checks the provided credentials against the database. If valid
    and the user is active, it utilizes the configured authentication backend
    to generate a session/token.

    Args:
        credentials (UserLogin): A Pydantic model containing the user's email and password.
        user_manager (UserManager): The user management service injected by FastAPI.

    Returns:
        Response: A FastAPI Response object containing the auth token (usually JSON for JWT).

    Raises:
        HTTPException(401): If authentication fails or the user is inactive.
    """
    # Attempt to authenticate the user using the provided credentials.
    user = await user_manager.authenticate_json(credentials)

    # Verify if the user exists and is active.
    # We use a generic error message to prevent user enumeration attacks.
    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    # Generate the login response (e.g., JWT token) using the transport backend.
    response = await auth_backend.login(auth_backend.get_strategy(), user)

    return response
