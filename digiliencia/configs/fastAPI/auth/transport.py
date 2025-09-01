# /auth/transport.py
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from core.config import settings

bearer_transport = BearerTransport(tokenUrl="/api/auth/login")


def get_jwt_strategy() -> JWTStrategy:
    """Returns the JWT strategy for encoding/decoding tokens."""
    return JWTStrategy(secret=settings.JWT_SECRET_KEY, lifetime_seconds=3600)


# The AuthenticationBackend is the main object for authentication logic
auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
