# /api/routers/auth.py
# All endpoints are async and refresh token logic is added
from fastapi import APIRouter, Depends, HTTPException, status, Response, Body, Request
from sqlalchemy.ext.asyncio import AsyncSession

from db import crud, session, models
from schemas import user as user_schema, token as token_schema
from core import security
from api.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=token_schema.Token)
async def login(
    request: Request,  # Needed for rate limiting
    db: AsyncSession = Depends(session.get_db),
    form_data: user_schema.UserLogin = Body(...),
):
    """User login to get access and refresh tokens."""
    user = await crud.get_user_by_email(db, email=form_data.email)
    if not user or not security.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    access_token = security.create_access_token(subject=user.email)
    refresh_token = security.create_refresh_token(subject=user.email)

    return {"access_token": access_token, "refresh_token": refresh_token}


# NEW: Endpoint to refresh the access token
@router.post("/refresh", response_model=token_schema.Token)
async def refresh_access_token(
    request: Request,
    refresh_request: token_schema.RefreshTokenRequest,
):
    """Get a new access token using a refresh token."""
    email = security.decode_refresh_token(refresh_request.refresh_token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = security.create_access_token(subject=email)
    # Optionally, issue a new refresh token as well for token rotation
    new_refresh_token = security.create_refresh_token(subject=email)

    return {"access_token": new_access_token, "refresh_token": new_refresh_token}


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
async def logout(current_user: models.User = Depends(get_current_user)):
    # To implement true server-side logout, a token blocklist would be needed (e.g., in Redis)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# The rest of the user routes need to be in their own file or adjusted
# and made async as well. For example:
users_router = APIRouter(prefix="/users", tags=["Users"])


@users_router.post(
    "/register", status_code=status.HTTP_201_CREATED, response_model=user_schema.User
)
async def register_user(
    request: Request,
    user: user_schema.UserRegister,
    db: AsyncSession = Depends(session.get_db),
):
    db_user = await crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    return await crud.create_user(db=db, user=user)
