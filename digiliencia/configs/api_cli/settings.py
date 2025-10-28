import httpx
from typing import Tuple, Callable, Dict

import auth
import auth_flow
import chat_flow


unauthenticated_routes: Dict[str, Callable[[httpx.Client], Tuple[bool, str]]] = {
    "login": auth_flow.login_flow,
    "register": auth_flow.register_flow,
    "show AI models": chat_flow.show_AI_models,
    "show_templates": chat_flow.show_templates,
}

authenticated_routes: Dict[str, Callable[[httpx.Client], Tuple[bool, str]]] = {
    "Log out": auth.logout,
    "Delete user": auth.delete_user,
    "New chat": chat_flow.create_chat_flow,
    "Select chat": chat_flow.select_chat,
    "Show chats": chat_flow.show_chats,
}
