import httpx
import uuid
from typing import Dict, Tuple, Optional

import chat
import menu


def create_chat_flow(
    client: httpx.Client, previous_message: Optional[str] = None
) -> Tuple[bool, Optional[str]]:
    tittle_key = "tittle"
    tittle: str = menu.input_menu({tittle_key: str}, "Creating a chat.")[tittle_key]
    # Invert keys and values: use template name as key and UUID as value
    templates = chat.get_templates(client)
    template_dict: Dict[str, uuid.UUID] = {
        v[0]: uuid.UUID(str(k)) for k, v in templates.items()
    }
    template: uuid.UUID = menu.selection(template_dict, previous_message)

    success, message = chat.create_chat(client, tittle, template)
    if success:
        return True, "Chat created."
    return False, message


def select_chat(
    client: httpx.Client, previous_message: Optional[str] = None
) -> Tuple[bool, Optional[str]]:
    chats: Dict[uuid.UUID, Tuple[str, uuid.UUID]] = chat.get_chats(client)
    selected_chat_id: uuid.UUID = menu.selection(chats, previous_message)
    selected_chat_id
    return True, None


def delete_chat_flow(
    client: httpx.Client, previous_message: Optional[str] = None
) -> Tuple[bool, Optional[str]]:
    chats: dict[uuid.UUID, Tuple[str, uuid.UUID]] = chat.get_chats(client)
    if not bool(chats):
        menu.alert("No chats found.")
    else:
        chat_id: uuid.UUID = menu.selection(
            {value[0]: key for key, value in chats.items()}, previous_message
        )
        if chat_id:
            success, messaje = chat.delete_chat(client, chat_id)
            if success:
                menu.alert("Chat deleted")
            else:
                menu.alert(f"Unenable delete chat. Error: {messaje}")
    return True, None


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


def show_chats(
    client: httpx.Client, previous_message: Optional[str] = None
) -> Tuple[bool, Optional[str]]:
    chats: Dict[uuid.UUID, Tuple[str, uuid.UUID]] = chat.get_chats(client)
    if not bool(chats):
        menu.alert("No chats found.")
    else:
        menu.iterables_show(
            chats.values(), ("Tittle", "Template"), previous_message, True
        )
    return True, None
