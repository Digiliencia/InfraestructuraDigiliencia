"""
Constants for API endpoints and routes.
"""

from typing import List, Optional
from fastapi import APIRouter
from enum import Enum

# Base API URLs
API_PREFIX = "/api"  # Matches the prefix in main.py

# Auth endpoints
AUTH_PATH = "/auth"
JWT_PATH = f"{API_PREFIX}{AUTH_PATH}/jwt"
LOGIN = f"{AUTH_PATH}/login"  # Becomes /api/auth/jwt/login
TOKEN = f"{JWT_PATH}/login"
REGISTER = "/register"  # Becomes /api/register
VERIFY = "/verify"  # Becomes /api/verify
USERS_PATH = "/users"
USERS_ME_PATH = "/me"  # Becomes /api/users/me
HEALTH_PATH = "/health"  # Becomes /api/health

CHATS_PATH = "/chats"  # Becomes /api/chats
CONVERSATIONS = "/conversations"  # Becomes /api/conversations
TEMPLATE_LIST = f"{CHATS_PATH}/template_list"  # Becomes /api/chats/template_list
MODEL_LIST = f"{CHATS_PATH}/model_list"  # Becomes /api/chats/model_list

# Health and root endpoints
ROOT = f"{API_PREFIX}/"  # Becomes /api/

HEALTH = f"{API_PREFIX}/health"  # Becomes /api/health

USERS_ME = f"{USERS_PATH}{USERS_ME_PATH}"


def get_prefixed_router(
    prefix: str = "", tags: Optional[List[str | Enum]] = None, **kwargs
) -> APIRouter:
    """
    Create a router with the API prefix already set.

    Args:
        prefix: Additional prefix to append after API_PREFIX
        tags: OpenAPI tags for the router
        **kwargs: Additional arguments to pass to APIRouter

    Returns:
        APIRouter: Configured router with the correct prefix
    """
    full_prefix = f"{API_PREFIX}{prefix}" if prefix else API_PREFIX
    return APIRouter(prefix=full_prefix, tags=tags, **kwargs)
