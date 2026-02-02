# chat.py
"""
API Client wrapper for Chat operations.

This module handles the HTTP communication with the Chat API endpoints,
serializing requests and validating responses using Pydantic schemas.
"""

import uuid
from typing import Optional, Tuple

import httpx
from pydantic import ValidationError
from starlette import status

# Custom modules
import menu  # Assumed to be available for UI alerts
from digiliencia.configs.fastAPI.core.endpoints import (
    CHATS_PATH,
    CONVERSATIONS,
    MODEL_LIST,
    TEMPLATE_LIST,
)
from digiliencia.configs.fastAPI.schemas import chat as chat_schema


class Chat:
    """
    Handles interaction with the Chat API endpoints.
    """

    def __init__(self, client: httpx.Client) -> None:
        """
        Args:
            client (httpx.Client): A configured HTTP client (base URL, auth headers, etc).
        """
        self.client: httpx.Client = client

    def create_chat(
        self, title: str, template_id: uuid.UUID
    ) -> Optional[chat_schema.ConversationSummary]:
        """
        Creates a new chat conversation.

        Args:
            title (str): The title of the chat.
            template_id (uuid.UUID): The ID of the AI Prompt/Template.

        Returns:
            Optional[ConversationSummary]: The created chat summary or None if failed.
        """
        # Update: Field name changed from 'ia_prompt' to 'ai_prompt_id'
        chat_data = {"title": title, "ai_prompt_id": str(template_id)}

        try:
            response = self.client.patch(CHATS_PATH, json=chat_data)

            if response.status_code == status.HTTP_201_CREATED:
                return chat_schema.ConversationSummary.model_validate(response.json())

            # Handle errors
            error_detail = response.json().get("detail", str(response.content))
            menu.alert(f"Failed to create chat: {error_detail}")

        except ValidationError as e:
            menu.alert(f"Validation error: {e}")
        except Exception as e:
            menu.alert(f"Network/Unexpected error: {e}")

        return None

    def get_chats(self) -> Optional[chat_schema.ConversationSummaries]:
        """
        Retrieves a list of all conversations for the user.
        """
        try:
            response = self.client.get(CONVERSATIONS)

            # Update: Backend now returns 200 OK for lists
            if response.status_code == status.HTTP_200_OK:
                return chat_schema.ConversationSummaries.model_validate(response.json())

            menu.alert(f"Error getting chats: {response.status_code}")

        except ValidationError as e:
            menu.alert(f"Schema validation error: {e}")
        except Exception as e:
            menu.alert(f"Error: {e}")

        return None

    def get_templates(self) -> Optional[chat_schema.Templates]:
        """
        Retrieves the list of available AI templates.
        """
        try:
            response = self.client.get(TEMPLATE_LIST)

            if response.status_code == status.HTTP_200_OK:
                return chat_schema.Templates.model_validate(response.json())

            menu.alert(f"Error getting templates: {response.status_code}")

        except ValidationError as e:
            menu.alert(f"Schema validation error: {e}")
        return None

    def get_AI_models(self) -> Optional[chat_schema.Models]:
        """
        Retrieves the list of available AI models.
        """
        try:
            response = self.client.get(MODEL_LIST)

            if response.status_code == status.HTTP_200_OK:
                return chat_schema.Models.model_validate(response.json())

            menu.alert(f"Error getting models: {response.status_code}")

        except ValidationError as e:
            menu.alert(f"Schema validation error: {e}")
        return None

    def delete_chat(self, chat_id: uuid.UUID) -> bool:
        """
        Deletes a specific chat.

        Args:
            chat_id (uuid.UUID): The ID of the chat to delete.
        """
        try:
            response = self.client.delete(f"{CHATS_PATH}/{str(chat_id)}")

            if response.status_code == status.HTTP_204_NO_CONTENT:
                return True
            elif response.status_code == status.HTTP_404_NOT_FOUND:
                menu.alert(f"Chat {chat_id} not found.")
            else:
                menu.alert(f"Error deleting chat: {response.status_code}")

        except Exception as e:
            menu.alert(f"Error: {e}")

        return False

    def get_chat(
        self, chat_id: uuid.UUID
    ) -> Tuple[Optional[Tuple[chat_schema.Message, ...]], str]:
        """
        Retrieves full details and message history of a chat.

        Returns:
            Tuple: (Tuple of Messages or None, Status Message)
        """
        try:
            response = self.client.get(f"{CHATS_PATH}/{str(chat_id)}")

            if response.status_code == status.HTTP_200_OK:
                # Validate full object using Pydantic
                full_conversation = chat_schema.ConversationFull.model_validate(
                    response.json()
                )
                return full_conversation.messages, "OK"

            elif response.status_code == status.HTTP_404_NOT_FOUND:
                return None, f"Chat {chat_id} not found."
            else:
                return None, f"API Error: {response.status_code}"

        except ValidationError as e:
            return None, f"Data validation error: {e}"
        except Exception as e:
            return None, f"Network error: {e}"

    def ask_question(
        self, question: str, chat_id: uuid.UUID, model_id: uuid.UUID
    ) -> Tuple[Optional[str], str]:
        """
        Sends a message to the chat and retrieves the AI response.

        Args:
            question (str): The user's text message.
            chat_id (uuid.UUID): The current chat ID.
            model_id (uuid.UUID): The AI model ID to use.

        Returns:
            Tuple[Optional[str], str]: (AI Response Text, Status/Error message)
        """
        message_payload = {"content": question, "model_id": str(model_id)}

        try:
            response = self.client.patch(
                f"{CHATS_PATH}/{str(chat_id)}", json=message_payload, timeout=1000
            )

            if response.status_code == status.HTTP_200_OK:
                # Validate response schema
                ai_resp = chat_schema.AIResponse.model_validate(response.json())
                return ai_resp.text, "OK"

            elif response.status_code == status.HTTP_404_NOT_FOUND:
                return None, "Chat not found."
            elif response.status_code == status.HTTP_409_CONFLICT:
                return None, "Chat is busy. Please wait."

            return None, f"API Error: {response.status_code}"

        except ValidationError:
            return None, "Invalid response format from server."
        except Exception as e:
            return None, f"Error: {e}"
