import auth
import auth_flow

import httpx
from typing import Tuple, Callable, Dict

unauthenticated_routes: Dict[str, Callable[[httpx.Client], Tuple[bool, str]]] = {
    "login": auth_flow.login_flow,
    "register": auth_flow.register_flow,
}

authenticated_routes: Dict[str, Callable[[httpx.Client], Tuple[bool, str]]] = {
    "log out": auth.logout,
    "delete user": auth.delete_user,
}
