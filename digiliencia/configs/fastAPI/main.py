# /main.py
"""
Main application entry point.

This module initializes the FastAPI application, configures middlewares (CORS, Security, RateLimit),
and mounts the API routers. It serves as the central hub for the backend service.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

# Auth & Core Imports
from auth.transport import auth_backend
from auth.users import fastapi_users
from core.config import settings
from core.endpoints import (
    API_PREFIX,
    AUTH_PREFIX,
    HEALTH_PATH,
    ROOT,
)

# Schema Imports
from schemas import user as user_schema

# Router Imports
from api.routers import chats, custom_auth, custom_users, models, templates

# --- Configuration ---

# Initialize Rate Limiter
limiter = Limiter(key_func=get_remote_address, default_limits=["1000 per minute"])

# Initialize App
app = FastAPI(
    title="Digiliencia Chat API",
    description="Backend API for AI-powered chat conversations.",
    version="2.0.0",
    docs_url=f"{API_PREFIX}/docs",
    redoc_url=f"{API_PREFIX}/redoc",
    openapi_url=f"{API_PREFIX}/openapi.json",
)

# Attach limiter to app state (required by slowapi)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# --- Middlewares ---

# 1. CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 2. Security Headers
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """
    Middleware to add security headers to every response.
    Enforces HSTS, CSP, and prevents content sniffing/framing.
    """
    response = await call_next(request)
    response.headers["Strict-Transport-Security"] = (
        "max-age=31536000; includeSubDomains"
    )
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    return response


# --- Routers Setup ---

# The strategy here is to mount everything under API_PREFIX (/api).
# Specific sub-paths are handled either by the router inclusion prefix
# or by the constants defined in core/endpoints.py used inside the routers.

# 1. Authentication Routers
# -------------------------

# Standard JWT Login (fastapi-users) -> /api/auth/jwt/login
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=f"{API_PREFIX}{AUTH_PREFIX}/jwt",
    tags=["Auth"],
)

# Registration (fastapi-users) -> /api/auth/register
app.include_router(
    fastapi_users.get_register_router(
        user_schema.UserRead,
        user_schema.UserRegistration,
    ),
    prefix=f"{API_PREFIX}{AUTH_PREFIX}",
    tags=["Auth"],
)

# Account Verification -> /api/auth/verify
app.include_router(
    fastapi_users.get_verify_router(user_schema.UserRead),
    prefix=f"{API_PREFIX}{AUTH_PREFIX}",
    tags=["Auth"],
)

# Custom Login (JSON) -> Defined in router as LOGIN (/auth/login) -> /api/auth/login
app.include_router(custom_auth.router, prefix=API_PREFIX, tags=["Auth"])


# 2. User Management
# ------------------
# Defined in router using USERS_ME (/users/me) -> /api/users/me
app.include_router(custom_users.router, prefix=API_PREFIX, tags=["Users"])


# 3. Chat & Content Routers
# -------------------------
# Templates -> /api/chats/templates
app.include_router(templates.router, prefix=API_PREFIX, tags=["Templates"])

# Models -> /api/chats/models
app.include_router(models.router, prefix=API_PREFIX, tags=["Models"])

# Chats -> Defined in router using CONVERSATIONS (/chats/conversations) -> /api/chats/...
app.include_router(chats.router, prefix=API_PREFIX, tags=["Chats"])

# --- Global Endpoints ---


@app.get(ROOT, tags=["Root"])
def read_root():
    return {"message": "Welcome to the Digiliencia Chat API v2"}


@app.get(f"{API_PREFIX}{HEALTH_PATH}", tags=["Health"])
def health():
    return {"status": "ok", "service": "fastapi-service"}
