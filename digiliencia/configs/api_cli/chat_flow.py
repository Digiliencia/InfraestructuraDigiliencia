import httpx
from starlette import status

from digiliencia.configs.fastAPI.core.endpoints import (
    CONVERSATIONS,
    TEMPLATE_LIST,
    MODEL_LIST,
)


def show_chats(client: httpx.Client) -> str:
    response = client.get(CONVERSATIONS)
    if response.status_code == status.HTTP_200_OK:
        conversations = response.json()
        if not conversations:
            return "No conversations found."
        message = "Conversations:\n"
        for convo in conversations:
            message += f"- ID: {convo['id']}, Title: {convo['title']}\n"
        return message
    return f"Failed to fetch conversations. Status code: {response.status_code}"


def show_templates(client: httpx.Client) -> str:
    response = client.get(TEMPLATE_LIST)
    if response.status_code == status.HTTP_202_ACCEPTED:
        templates = response.json()
        if not templates:
            return "No templates found."
        message = "Available Templates:\n"
        for template in templates:
            message += f"- ID: {template['id']}, Name: {template['name']}\n"
        return message
    return f"Failed to fetch templates. Status code: {response.status_code}"


def show_IA_models(client: httpx.Client) -> str:
    response = client.get(MODEL_LIST)
    if response.status_code == status.HTTP_202_ACCEPTED:
        models = response.json()
        if not models:
            return "No AI models found."
        message = "Available AI Models:\n"
        for model in models:
            message += f"- ID: {model['id']}, Name: {model['name']}\n"
        return message
    return f"Failed to fetch AI models. Status code: {response.status_code}"
