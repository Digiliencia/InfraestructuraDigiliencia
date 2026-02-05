# /api/v2/users.py
from fastapi import APIRouter, Depends
from schemas.user import UserRead, UserUpdate
from db.models import User
from auth.users import fastapi_users
from auth.manager import get_user_manager, UserManager
from api.routers.custom_users import get_my_data, update_my_data, delete_my_data, logout

current_user = fastapi_users.current_user(active=True)
router = APIRouter(dependencies=[Depends(current_user)])


@router.get(
    "/v2/users/me", response_model=UserRead, summary="Get Current User Profile (V2)"
)
async def v2_get_my_data(user: User = Depends(current_user)):
    return await get_my_data(user)


@router.patch(
    "/v2/users/me", response_model=UserRead, summary="Update Current User Profile (V2)"
)
async def v2_update_my_data(
    payload: UserUpdate,
    user: User = Depends(current_user),
    user_manager: UserManager = Depends(get_user_manager),
):
    return await update_my_data(payload, user, user_manager)


@router.delete(
    "/v2/users/me", status_code=204, summary="Delete Current User Account (V2)"
)
async def v2_delete_my_data(
    user: User = Depends(current_user),
    user_manager: UserManager = Depends(get_user_manager),
):
    return await delete_my_data(user, user_manager)


@router.post("/v2/users/me", summary="Logout User (V2)")
async def v2_logout(user: User = Depends(current_user)):
    return await logout(user)
