# auth/users.py
import uuid
from fastapi_users import FastAPIUsers
from auth.manager import get_user_manager
from auth.transport import auth_backend
from db.models import User

# --- Configuración de FastAPI-Users ---
fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
