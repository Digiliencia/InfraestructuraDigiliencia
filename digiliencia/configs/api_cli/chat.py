import httpx
from starlette import status
import uuid
from typing import Tuple, Optional

from pydantic import ValidationError

import menu
from digiliencia.configs.fastAPI.core.endpoints import (
    CONVERSATIONS,
    TEMPLATE_LIST,
    MODEL_LIST,
    CHATS_PATH,
)

import digiliencia.configs.fastAPI.schemas.chat as chat_schema


class Chat:
    def __init__(self, client: httpx.Client) -> None:
        self.client: httpx.Client = client

    def create_chat(
        self, tittle: str, template_id: uuid.UUID
    ) -> Optional[chat_schema.ConversationSummary]:
        chat_data = {"tittle": tittle, "ia_prompt": str(template_id)}
        chat_response = self.client.patch(CHATS_PATH, json=chat_data)
        if chat_response.status_code == status.HTTP_201_CREATED:
            try:
                summary: chat_schema.ConversationSummary = (
                    chat_schema.ConversationSummary.model_validate(chat_response.json())
                )
                return summary
            except ValidationError as e:
                menu.alert(str(e))
        else:
            menu.alert(chat_response.json())
        return None

    def get_chats(self) -> Optional[chat_schema.ConversationSummaries]:
        response = self.client.get(CONVERSATIONS)
        if response.status_code != status.HTTP_202_ACCEPTED:
            raise Exception(response.json())
        try:
            conversations: chat_schema.ConversationSummaries = (
                chat_schema.ConversationSummaries.model_validate(response.json())
            )
            return conversations
        except ValidationError as e:
            menu.alert(str(e))

        return None

    def get_templates(self) -> Optional[chat_schema.Templates]:
        response = self.client.get(TEMPLATE_LIST)
        if response.status_code == status.HTTP_202_ACCEPTED:
            templates = response.json()
            if templates:
                try:
                    return chat_schema.Templates.model_validate(templates)
                except ValidationError as e:
                    menu.alert(str(e))
        return None

    def get_AI_models(self) -> Optional[chat_schema.Models]:
        response = self.client.get(MODEL_LIST)
        if response.status_code == status.HTTP_202_ACCEPTED:
            models = response.json()
            if models:
                try:
                    return chat_schema.Models.model_validate(models)
                except ValidationError as e:
                    menu.alert(str(e))
        return None

    def delete_chat(self, chat_id: uuid.UUID) -> bool:
        response = self.client.delete(f"{CHATS_PATH}/{str(chat_id)}")
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return True
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            menu.alert(f"Chat {chat_id} not found.")
            return False
        menu.alert(f"Unexpected error: {response} for chat {chat_id}")
        return False

    def get_chat(self, chat_id: uuid.UUID) -> Tuple[Optional[list[str]], str]:
        response = self.client.get(f"{CHATS_PATH}/{str(chat_id)}")
        if response.status_code == status.HTTP_202_ACCEPTED:
            messages = response.json()
            message_list: list[str] = list()
            for message in messages["messages"]:
                message_list.append(message)
            return message_list, "OK"
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            return None, f"Chat {chat_id} not found."
        return None, f"Unexpected error: {response} for chat {chat_id}"

    def ask_question(
        self, question: str, chat_id: uuid.UUID, ia_model: uuid.UUID
    ) -> Tuple[Optional[str], str]:
        message_content = {"text": question, "model_id": str(ia_model)}
        response = self.client.patch(
            f"{CHATS_PATH}/{str(chat_id)}", json=message_content
        )
        if response.status_code == status.HTTP_202_ACCEPTED:
            message: str = response.json()["text"]
            return message, "OK"
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            return None, f"Chat {chat_id} not found."
        return None, f"Unexpected error: {response} for chat {chat_id}"
