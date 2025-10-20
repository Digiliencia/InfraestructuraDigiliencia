# /auth/users.py
"""
This module configures and initializes the main FastAPIUsers instance.

It brings together the user manager, authentication backends, and the User
model to create a central `fastapi_users` object. This object is then used
by the main application to generate the various authentication-related
API routers (e.g., for registration, login, verification).
"""

import uuid
from fastapi_users import FastAPIUsers

from auth.manager import get_user_manager
from auth.transport import auth_backend
from db.models import User

# --- FastAPI-Users Configuration ---

# This is the central object that orchestrates the fastapi-users library.
# It is a generic class that requires the User model type and the user ID type.
# - get_user_manager: A dependency that provides the UserManager instance for
#   handling user business logic.
# - [auth_backend]: A list of one or more authentication backends that define
#   how users can authenticate (in this case, via JWT Bearer tokens).
fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
