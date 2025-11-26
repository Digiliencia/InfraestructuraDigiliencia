# /core/endpoints.py
"""
API Route Constants.

This module acts as the Single Source of Truth for all API path definitions.
"""

from typing import Final, List, Optional, Union
from fastapi import APIRouter
from enum import Enum

# --- Global Prefix ---
API_PREFIX: Final[str] = "/api"

# --- Authentication Routes ---
# Prefix: /api/auth
AUTH_PREFIX: Final[str] = "/auth"

# Endpoint: /api/auth/login (POST)
LOGIN: Final[str] = f"{AUTH_PREFIX}/login"

# Endpoint: /api/auth/register (POST)
REGISTER: Final[str] = f"{AUTH_PREFIX}/register"

# Endpoint: /api/auth/jwt/login (Standard FastAPI Users path)
TOKEN: Final[str] = f"{AUTH_PREFIX}/jwt/login"


# --- User Management Routes ---
# Prefix: /api/users
USERS_PREFIX: Final[str] = "/users"

# Endpoint: /api/users/me
USERS_ME: Final[str] = f"{USERS_PREFIX}/me"


# --- Chat & Conversation Routes ---
# Prefix: /api/chats
CHATS_PATH: Final[str] = "/chats"

# Endpoint: /api/chats/conversations
CONVERSATIONS: Final[str] = f"{CHATS_PATH}/conversations"

# Endpoint: /api/chats/templates
TEMPLATE_LIST: Final[str] = f"{CHATS_PATH}/templates"

# Endpoint: /api/chats/models
MODEL_LIST: Final[str] = f"{CHATS_PATH}/models"


# --- System & Root Endpoints ---

# Endpoint: /api/health
HEALTH_PATH: Final[str] = "/health"
HEALTH: Final[str] = f"{API_PREFIX}{HEALTH_PATH}"

# Endpoint: /api/ (API Root)
ROOT: Final[str] = f"{API_PREFIX}/"


# --- Helper Utilities ---


def get_prefixed_router(
    prefix: str = "", tags: Optional[List[Union[str, Enum]]] = None, **kwargs
) -> APIRouter:
    """
    Factory function to create an APIRouter with the global API_PREFIX applied.
    """
    full_prefix = f"{API_PREFIX}{prefix}" if prefix else API_PREFIX
    return APIRouter(prefix=full_prefix, tags=tags, **kwargs)
