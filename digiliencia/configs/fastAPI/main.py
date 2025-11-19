# /main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from auth.users import fastapi_users
from auth.transport import auth_backend
from core.endpoints import API_PREFIX, JWT_PATH, HEALTH, ROOT


from schemas import user as user_schema
from api.routers import chats, custom_users, custom_auth, models, templates
from core.config import settings

limiter = Limiter(key_func=get_remote_address, default_limits=["1000 per minute"])

app = FastAPI(title="API", description="API for AI.", version="1.0.0")

# --- Middlewares ---
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# 1. CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 2. Security headers
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["Strict-Transport-Security"] = (
        "max-age=31536000; includeSubDomains"
    )
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response


# --- Routers ---

# Endpoints from fastapi-users

# /api/auth/jwt/login
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=JWT_PATH,
    tags=["Auth"],
)

# /login
app.include_router(custom_auth.router, prefix=API_PREFIX, tags=["Auth"])

# /register
app.include_router(
    fastapi_users.get_register_router(
        user_schema.UserRead,
        user_schema.UserRegistration,  # type: ignore
    ),
    prefix=API_PREFIX,
    tags=["Auth"],
)

# /verify
app.include_router(
    fastapi_users.get_verify_router(user_schema.UserRead),
    prefix=API_PREFIX,
    tags=["Auth"],
)

# Public
app.include_router(models.router, prefix=API_PREFIX, tags=["Models"])
app.include_router(templates.router, prefix=API_PREFIX, tags=["templates"])

# Authentication required
app.include_router(custom_users.router, prefix=API_PREFIX, tags=["Users"])
app.include_router(chats.router, prefix=API_PREFIX, tags=["Chats"])


@app.get(ROOT, tags=["Root"])
def read_root():
    """
    Root endpoint that provides a welcome message.

    Returns:
        dict: A welcome message for the Chat API
    """
    return {"message": "Welcome to the Chat API"}


@app.get(HEALTH, tags=["Health"])
def health():
    """Simple health check endpoint.
    Returns a small JSON payload indicating the service is reachable.
    """
    return {"status": "ok"}
