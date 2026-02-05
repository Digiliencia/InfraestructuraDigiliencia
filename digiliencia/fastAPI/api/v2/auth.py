# /api/v2/auth.py
from fastapi import APIRouter, Depends, Response
from auth.manager import get_user_manager, UserManager
from schemas.user import UserLogin, UserRead, UserRegistration
from api.routers.custom_auth import login_with_json
from auth.transport import auth_backend
from auth.users import fastapi_users

router = APIRouter()

@router.post("/v2/auth/login", summary="User Login (V2)")
async def v2_login_with_json(credentials: UserLogin, user_manager: UserManager = Depends(get_user_manager)) -> Response:
    return await login_with_json(credentials, user_manager)

router.include_router(fastapi_users.get_register_router(UserRead, UserRegistration), prefix="/v2/auth", tags=["Auth V2"])
router.include_router(fastapi_users.get_verify_router(UserRead), prefix="/v2/auth", tags=["Auth V2"])
router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/v2/auth/jwt", tags=["Auth V2"])
