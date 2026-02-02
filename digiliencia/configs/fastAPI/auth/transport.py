# /auth/transport.py
"""
This module configures the authentication transport and backend for fastapi-users.

It assembles the authentication pipeline by combining:
1. **Transport:** How the token is transferred (Bearer Token in Headers).
2. **Strategy:** How the token is generated and validated (JWT).

These components create the `auth_backend` used to protect API routes.
"""

from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from core.config import settings
from core.endpoints import TOKEN

# Configure the Bearer Transport.
# This tells FastAPI that clients must send the token in the Authorization header:
# Authorization: Bearer <token>
# 'tokenUrl' points to the login endpoint for Swagger UI integration.
bearer_transport = BearerTransport(tokenUrl=TOKEN)


def get_jwt_strategy() -> JWTStrategy:
    """
    Provides the JWT strategy configuration for token generation and validation.

    The strategy defines:
    - The encryption algorithm (HS256 by default).
    - The secret key used to sign the tokens.
    - The expiration time (lifetime) of the tokens.

    Returns:
        JWTStrategy: A configured instance of the JWT strategy.
    """
    return JWTStrategy(
        secret=settings.JWT_SECRET_KEY,
        lifetime_seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS,
    )


# The AuthenticationBackend combines the transport and strategy.
# It is the main object passed to the fastapi_users router generator.
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
