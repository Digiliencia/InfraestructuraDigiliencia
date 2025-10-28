import httpx
import uuid
from typing import Dict, Tuple, Optional, Tuple

from digiliencia.configs.fastAPI.core.endpoints import (
    CONVERSATIONS,
    TEMPLATE_LIST,
    MODEL_LIST,
)
import chat
import menu


def create_chat_flow(
    client: httpx.Client, previous_message: Optional[str] = None
) -> str:
    pass


def select_chat(client: httpx.Client, previous_message: Optional[str] = None) -> str:
    pass


def show_templates(
    client: httpx.Client, previous_message: Optional[str] = None
) -> Tuple[bool, Optional[str]]:
    templates: dict = chat.get_templates(client)
    print(previous_message)
    if not bool(templates):
        menu.alert("Template list is empty.")
    else:
        menu.iterables_show(templates.values(), ("Name", "Description"), is_pasue=True)
    return True, None


def show_AI_models(
    client: httpx.Client, previous_message: Optional[str] = None
) -> Tuple[bool, Optional[str]]:
    models: Dict[uuid.UUID, Tuple[str]] = chat.get_AI_models(client)
    if not bool(models):
        menu.alert("AI models list is empty.")
    else:
        menu.iterables_show(models.values(), ("Name", "Description"), is_pasue=True)
    return True, None


def show_chats(client: httpx.Client, previous_message: Optional[str] = None) -> Tuple[bool, Optional[str]]:
    pass
