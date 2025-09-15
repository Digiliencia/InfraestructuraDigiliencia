# /api/routers/custom_auth.py

from fastapi import APIRouter, Depends, HTTPException, status
from auth.manager import get_user_manager, UserManager
from schemas.user import UserLogin
from auth.transport import auth_backend


router = APIRouter()


@router.post("/auth/login")
async def login_with_json(
    credentials: UserLogin,
    user_manager: UserManager = Depends(get_user_manager),
):
    """
    Login a user.
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
