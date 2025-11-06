import httpx
from starlette import status
import uuid
from typing import Tuple, Dict, Optional

from digiliencia.configs.fastAPI.core.endpoints import (
    CONVERSATIONS,
    TEMPLATE_LIST,
    MODEL_LIST,
    CHATS_PATH,
)


class Chat:
    def __init__(self, client: httpx.Client) -> None:
        self.client: httpx.Client = client

    def create_chat(self, tittle: str, template_id: uuid.UUID) -> Tuple[bool, str]:
        chat_data = {"tittle": tittle, "ia_prompt": str(template_id)}
        chat_response = self.client.patch(CHATS_PATH, json=chat_data)
        if chat_response.status_code == status.HTTP_201_CREATED:
            return True, chat_response.json()
        return False, chat_response.json()

    def get_chats(self) -> Dict[uuid.UUID | str, Tuple[str, uuid.UUID]]:
        response = self.client.get(CONVERSATIONS)
        chat_dict: Dict[uuid.UUID | str, Tuple[str, uuid.UUID]] = dict()
        if response.status_code == status.HTTP_202_ACCEPTED:
            conversations = response.json().get("conversations", [])
            if conversations:
                for convo in conversations:
                    chat_dict[uuid.UUID(convo["idChat"])] = (
                        convo["tittle"],
                        uuid.UUID(convo["template"]),
                    )
        else:
            print(response)
            raise Exception(response.json())
        return chat_dict

    def get_templates(self) -> Dict[uuid.UUID, Tuple[str, str]]:
        response = self.client.get(TEMPLATE_LIST)
        template_dict: dict[uuid.UUID, Tuple[str, str]] = dict()
        if response.status_code == status.HTTP_202_ACCEPTED:
            templates = response.json()
            if not templates:
                return template_dict
            for template in templates:
                template_dict[uuid.UUID(template["idTemplate"])] = (
                    template["template_name"],
                    template["template_description"],
                )
        else:
            raise Exception(response.json())
        return template_dict

    def get_AI_models(self) -> Dict[uuid.UUID, Tuple[str]]:
        response = self.client.get(MODEL_LIST)
        model_dict: dict[uuid.UUID, Tuple[str]] = dict()
        if response.status_code == status.HTTP_202_ACCEPTED:
            models = response.json()
            if not models:
                return model_dict
            for model in models:
                model_dict[uuid.UUID(model["idModel"])] = (model["model_name"],)
        else:
            raise Exception(response.json())
        return model_dict

    def delete_chat(self, chat_id: uuid.UUID) -> Tuple[bool, Optional[str]]:
        response = self.client.delete(f"{CHATS_PATH}/{str(chat_id)}")
        if response.status_code == status.HTTP_204_NO_CONTENT:
            return True, None
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            return False, f"Chat {chat_id} not found."
        return False, f"Unexpected error: {response} for chat {chat_id}"

    def get_chat(self, chat_id: uuid.UUID) -> Tuple[Optional[list[str]], str]:
        response = self.client.get(f"{CHATS_PATH}/{str(chat_id)}")
        if response.status_code == status.HTTP_202_ACCEPTED:
            messages = response.json()
            message_list: list[str] = list()
            for message in messages:
                message_list.append(message[2])
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
