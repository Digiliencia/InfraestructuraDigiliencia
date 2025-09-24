# /api/routers/custom_auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from auth.manager import get_user_manager, UserManager
from schemas.user import UserLogin
from auth.transport import auth_backend


router = APIRouter()


@router.post(
    "/auth/login",
    summary="Login with Email",
    description="Authenticate a user using email and password credentials",
    response_description="JWT token for authenticated user",
    responses={
        200: {
            "description": "Successful authentication",
            "content": {
                "application/json": {
                    "example": {
                        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                        "token_type": "bearer",
                    }
                }
            },
        },
        401: {
            "description": "Authentication failed",
            "content": {
                "application/json": {
                    "example": {"detail": "Incorrect email or password"}
                }
            },
        },
        422: {
            "description": "Validation error",
            "content": {
                "application/json": {"example": {"detail": "Invalid email format"}}
            },
        },
    },
)
async def login_with_json(
    credentials: UserLogin,
    user_manager: UserManager = Depends(get_user_manager),
):
    """
    Authenticate a user with email and password to obtain a JWT token.

    This endpoint validates the user credentials and returns a JWT token for authenticated access.
    The token should be included in subsequent requests in the Authorization header.

    Parameters:
        credentials (UserLogin): User login credentials
            - email: User's registered email address
            - password: User's password (min length: 8)
        user_manager (UserManager): User management service (injected)

    Returns:
        dict: Authentication response containing:
            - access_token (str): JWT token for API access
            - token_type (str): Token type (always "bearer")

    Raises:
        HTTPException:
            - 401: Invalid credentials or inactive user
            - 422: Invalid email format or password requirements not met

    Example:
        Request Body:
        ```json
        {
            "email": "user@example.com",
            "password": "secure_password"
        }
        ```

        Response:
        ```json
        {
            "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
            "token_type": "bearer"
        }
        ```

    Note:
        The returned JWT token must be included in the Authorization header
        of subsequent requests as: `Authorization: Bearer <token>`
    """
    # 2. Default authentication logic from fastapi-users
    user = await user_manager.authenticate_json(credentials)

    if not user or not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    # 3. Default login response from fastapi-users
    response = await auth_backend.login(auth_backend.get_strategy(), user)

    return response
