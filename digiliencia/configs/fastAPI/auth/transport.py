# /auth/transport.py
"""
This module configures the authentication transport and backend for fastapi-users.

It sets up the mechanism for how authentication tokens are transmitted (Bearer
transport) and how they are generated and validated (JWT strategy). These
components are combined into a single `auth_backend` instance that is used
by the application's authentication routers.
"""

from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from core.config import settings
from core.endpoints import TOKEN

# Defines the transport mechanism for authentication tokens.
# A BearerTransport expects tokens to be sent in the 'Authorization' header
# with the 'Bearer' prefix (e.g., "Authorization: Bearer <token>").
# The tokenUrl specifies the endpoint where clients can obtain a token.
bearer_transport = BearerTransport(tokenUrl=TOKEN)


def get_jwt_strategy() -> JWTStrategy:
    """
    Dependency that provides the JWT strategy for encoding/decoding tokens.

    The JWT strategy defines the algorithm and secret key used to create and
    verify JSON Web Tokens, as well as their expiration time.

    Returns:
        JWTStrategy: A configured instance of the JWT strategy.
    """
    return JWTStrategy(secret=settings.JWT_SECRET_KEY, lifetime_seconds=3600)


# The AuthenticationBackend is the main object that combines the transport
# (how tokens are sent) and the strategy (how tokens are managed) into a
# single, usable authentication mechanism for the application's endpoints.
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
