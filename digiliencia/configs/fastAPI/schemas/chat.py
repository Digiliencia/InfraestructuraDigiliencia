# /schemas/chat.py
"""
This module defines the Pydantic models (schemas) used for data validation,
serialization, and documentation in the chat-related API endpoints.

These schemas ensure that data exchanged between the client and the server
conforms to a predefined structure, enhancing type safety and clarity.
"""

from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID


class Text(BaseModel):
    """
    Schema for a single message payload sent by a user to an existing chat.

    Attributes:
        model_id (Optional[UUID]): The unique identifier of the AI model to be
                                   used for generating a response.
        text (str): The text content of the user's message.
    """

    model_id: Optional[UUID]
    text: str


class ChatCreate(BaseModel):
    """
    Schema for creating a new chat conversation.

    Attributes:
        tittle (str): The title for the new chat.
        ia_prompt (Optional[UUID]): The unique identifier of the IAPrompt
                                    template to associate with the chat. If
                                    omitted, a default prompt is used.
    """

    tittle: str
    ia_prompt: Optional[UUID] = None


class Texts(BaseModel):
    """
    A simple schema representing a piece of text, typically used in a list.

    Attributes:
        text (str): The content of the text.
    """

    text: str


class message(BaseModel):
    """
    Schema representing a single message within a full conversation history.

    Attributes:
        id (UUID): The unique identifier for the message.
        order_number (int): The sequence number of the message within the chat.
        content (str): The text content of the message.
        model_id (Optional[UUID]): The ID of the AI model that generated this
                                   message (if applicable).
    """

    id: UUID
    order_number: int
    content: str
    model_id: Optional[UUID]


class Captcha(BaseModel):
    """
    Schema for a captcha verification token.

    Attributes:
        captcha (str): The captcha token string provided by the user.
    """

    captcha: str


class ConversationSummary(BaseModel):
    """

    Schema for a brief summary of a chat conversation.

    Attributes:
        idChat (UUID): The unique identifier for the chat.
        tittle (str): The title of the chat.
        template (UUID): The unique identifier of the associated AI prompt.
    """

    idChat: UUID
    tittle: str
    template: UUID


class ConversationFull(ConversationSummary):
    """
    Schema for a complete chat conversation, including all its messages.

    Inherits all fields from `ConversationSummary`.

    Attributes:
        messages (List[message]): A list of all messages in the conversation,
                                  ordered by their sequence number.
    """

    messages: List[message]


class ConversationSummaries(BaseModel):
    """
    Schema for a response containing a tuple of conversation summaries.

    Attributes:
        conversations (Tuple[ConversationSummary,...]): The tuple of chat summaries.
    """

    conversations: tuple[ConversationSummary, ...]


class ConversationList(BaseModel):
    """
    Schema for a response containing a list of full conversations.

    Attributes:
        conversations (List[ConversationFull]): The list of full conversations.
    """

    conversations: List[ConversationFull]


class ConversationImport(BaseModel):
    """
    Schema for importing a new conversation from a list of texts.

    Attributes:
        ia_prompt (Optional[UUID]): The ID of the prompt template to use. If
                                    omitted, a default is assigned.
        tittle (str): The title for the newly imported chat.
        texts (List[Texts]): The list of messages to import into the new chat.
    """

    ia_prompt: Optional[UUID] = None
    tittle: str
    texts: List[Texts]


class ModelSummary(BaseModel):
    """
    Schema for a summary of an available AI model.

    Attributes:
        idModel (UUID): The unique identifier of the AI model.
        model_name (str): The display name of the AI model.
    """

    idModel: UUID
    model_name: str


class ModelList(BaseModel):
    """
    Schema for a response containing a list of available AI models.

    Attributes:
        models (tuple[ModelSummary, ...]): A tuple of AI model summaries.
    """

    models: tuple[ModelSummary, ...]


class TemplateSummary(BaseModel):
    """
    Schema for a summary of an available AI prompt template.

    Attributes:
        idTemplate (UUID): The unique identifier of the template.
        template_name (str): The display name of the template.
        template_description (str): A brief description of the template's purpose.
    """

    idTemplate: UUID
    template_name: str
    template_description: str


class TemplateList(BaseModel):
    """
    Schema for a response containing a list of available AI prompt templates.

    Attributes:
        templates (tuple[TemplateSummary, ...]): A tuple of template summaries.
    """

    templates: tuple[TemplateSummary, ...]
