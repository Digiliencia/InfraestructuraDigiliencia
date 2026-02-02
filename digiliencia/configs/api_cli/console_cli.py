# console_cli.py
"""
Main controller for the Command Line Interface (CLI).

This module handles the user interaction flow, menu rendering, and orchestration
of API calls via the Chat and Authentication services.
"""

from __future__ import (
    annotations,
)  # Allows using ConsoleCLI as a type hint inside the class

import os
import uuid
from typing import Callable, List, Optional, Tuple

import httpx
from starlette import status

from digiliencia.configs.fastAPI.schemas import chat as chat_schema
from digiliencia.configs.fastAPI.core.endpoints import HEALTH_PATH

# Custom modules
import menu
import authentication
from chat import Chat



def clear_screen():
    """Clears the console screen in a cross-platform way."""
    os.system("cls" if os.name == "nt" else "clear")


class ConsoleCLI:
    """
    Manages the state and flow of the CLI application.
    """

    def __init__(self, url: str) -> None:
        """
        Initializes the CLI client.

        Args:
            url (str): The base URL of the API.
        """
        self.messages: List[str] = ["Diligencia CLI"]
        self.base_url = url
        # Set a timeout to avoid hanging indefinitely
        self.client: httpx.Client = httpx.Client(base_url=url, timeout=10.0, verify=False)
        self.chat: Chat = Chat(self.client)
        self.alert_time: float = 1.5
        self._check_health()

    def _check_health(self) -> None:
        """Performs an initial health check on the API."""
        try:
            response = self.client.get(HEALTH_PATH)
            if response.status_code != status.HTTP_200_OK:
                print(f"[!] API Warning: Status code {response.status_code}")
            elif response.json().get("status") != "ok":
                print("[!] API Warning: Health status is not 'ok'.")
        except httpx.RequestError as e:
            print(f"[!] Critical: Could not connect to API at {self.base_url}")
            print(f"    Error: {e}")
            input("Press Enter to retry anyway (or Ctrl+C to exit)...")
            self._check_health()
        except Exception as e:
            print(f"[!] Unexpected error during health check: {e}")

    def is_logged_in(self) -> bool:
        """
        Checks if the user has an active session token.
        Updates the available routes based on auth status.
        """
        logged: bool = self.client.headers.get("Authorization") is not None
        self.routes: Tuple[Tuple[str, Callable[[ConsoleCLI], None]], ...] = (
            AUTHENTICATED_ROUTES if logged else UNAUTHENTICATED_ROUTES
        )
        return logged

    def initial_menu_flow(self) -> None:
        """Main application loop."""
        while True:
            clear_screen()
            self.is_logged_in()

            # Displays the main menu
            selected_action: Optional[Callable[[ConsoleCLI], None]] = menu.selection(
                self.routes,
                self.messages,
            )

            clear_screen()

            if selected_action is None:
                break

            # Execute the selected function passing the CLI instance
            selected_action(self)

        if self.is_logged_in():
            self.logout()
        print("Exiting application.")

    def login_flow(self) -> None:
        """Handles the user login process."""
        max_try = 3
        counter = max_try
        try:
            while counter > 0:
                inputs = menu.input_menu({"email": str, "password": str}, self.messages)
                if authentication.login(
                    self.client, inputs["email"], inputs["password"]
                ):
                    self.messages.append(f"Logged as: {inputs['email']}")
                    menu.alert("Login successful.", self.alert_time)
                    return

                counter -= 1
                if counter > 0:
                    menu.alert(
                        f"Login failed. {counter} attempts remaining.", self.alert_time
                    )

            menu.alert("Maximum login attempts exceeded.", self.alert_time * 2)

        except KeyboardInterrupt:
            return

    def register_flow(self, message: Optional[str] = None) -> None:
        """Handles user registration."""
        try:
            inputs = menu.input_menu(
                {"email": str, "password": str}, self.messages, message
            )
        except KeyboardInterrupt:
            return

        if authentication.register(self.client, inputs["email"], inputs["password"]):
            # Auto-login after registration
            if not authentication.login(
                self.client, inputs["email"], inputs["password"]
            ):
                menu.alert(
                    "Registration succeeded but automatic login failed. Please login manually.",
                    self.alert_time,
                )
            else:
                self.messages.append(f"Logged as: {inputs['email']}")
                menu.alert("Registration and login successful.", self.alert_time)

    def delete_user(self) -> None:
        """Deletes the current user account."""
        if menu.confirm("Are you sure you want to delete your account?"):
            authentication.delete_user(self.client)
            self.messages.pop()

    def logout(self) -> None:
        """Logs out the current user."""
        if authentication.logout(self.client):
            # Safely remove the "Logged as" message if it exists
            if len(self.messages) > 1:
                self.messages.pop()

    def create_chat_flow(self) -> None:
        """Flow to create a new chat conversation."""
        title_key = "title"
        try:
            user_input = menu.input_menu(
                {title_key: str}, self.messages, "Creating a chat."
            )
            title = user_input[title_key]
        except KeyboardInterrupt:
            return

        templates = self.chat.get_templates()
        if templates is None or not templates.templates:
            menu.alert("Error getting templates or no templates available.")
            return

        selected_template_id: uuid.UUID = menu.selection(
            tuple(
                (f"{t.name} - {t.description}", str(t.id)) for t in templates.templates
            ),
            self.messages,
        )

        if selected_template_id and self.chat.create_chat(title, selected_template_id):
            menu.alert("Chat created.", self.alert_time)

    def select_chat_flow(self) -> None:
        """Flow to select and enter a chat."""
        chats: Optional[chat_schema.ConversationSummaries] = self.chat.get_chats()

        if chats is None or not chats.conversations:
            menu.alert("Chats not found or list is empty.")
            return

        # Helper to resolve template names for display
        templates = self.chat.get_templates()
        template_map = {t.id: t.name for t in templates.templates} if templates else {}

        # Updated to match new Schema: chat.title and chat.id
        selected_chat_id: uuid.UUID = menu.selection(
            tuple(
                (
                    f"{chat.title} [{template_map.get(chat.ai_prompt_id, 'Unknown')}]",
                    str(chat.id),
                )
                for chat in chats.conversations
            ),
            self.messages,
        )

        if selected_chat_id is None:
            return

        chat_obj, error_msg = self.chat.get_chat(selected_chat_id)
        if chat_obj is None:
            menu.alert(f"Error loading chat: {error_msg}")
            return

        self.conversation_flow(chat_obj, selected_chat_id)

    def conversation_flow(
        self,
        chat_messages: Tuple[chat_schema.Message, ...],
        selected_chat_id: uuid.UUID,
    ) -> None:
        """
        Handles the actual chat interaction loop.

        Args:
            chat_messages: The initial history of messages.
            selected_chat_id: The ID of the active chat.
        """
        # Get available models for the response
        ai_models = self.chat.get_AI_models()
        if ai_models is None or not ai_models.models:
            menu.alert("No AI models available to reply.")
            return

        # Ask user to select a model
        print("\n[!] Select an AI model for this conversation:")
        target_model_id = menu.selection(
            tuple((model.name, model.id) for model in ai_models.models), self.messages
        )

        if target_model_id is None:
            return

        formatted_history = [
            f"{'User' if msg.model_id is None else 'AI'}: {msg.content}"
            for msg in chat_messages
        ]

        message_label = "Message"
        while True:
            try:
                self.show_header()
                menu.iterables_show(formatted_history, is_pasue=False, clean=False)
                user_input = menu.input_menu({message_label: str}, clean=False)
                message_text = user_input[message_label]
            except KeyboardInterrupt:
                break
            # Send message to API
            response_text, error = self.chat.ask_question(
                message_text, selected_chat_id, target_model_id
            )
            if response_text is None:
                # Show error and allow user to retry
                menu.alert(f"Error: {error}")
                continue

            # Attempt to reload the full conversation from server
            chat_obj, err_msg = self.chat.get_chat(selected_chat_id)
            if chat_obj is None:
                # Fallback: append the local exchange
                formatted_history.append(f"User: {message_text}")
                formatted_history.append(f"AI: {response_text}")
                # Refresh display
                self.show_header()
                menu.iterables_show(formatted_history, is_pasue=False, clean=False)
            else:
                # Build history from server-provided messages
                formatted_history = [
                    f"{'User' if msg.model_id is None else 'AI'}: {msg.content}"
                    for msg in chat_obj
                ]
                # Refresh display with authoritative history
                self.show_header()
                menu.iterables_show(formatted_history, is_pasue=False, clean=False)

    def delete_chat_flow(self) -> None:
        """Flow to delete a chat."""
        chats = self.chat.get_chats()
        if chats is None or not chats.conversations:
            menu.alert("Chats not found")
            return

        selected_chat: chat_schema.ConversationSummary = menu.selection(
            tuple((f"{chat.title}", chat) for chat in chats.conversations),
            self.messages,
        )

        if selected_chat and self.chat.delete_chat(selected_chat.id):
            menu.alert(f"Chat '{selected_chat.title}' deleted", self.alert_time)

    def show_templates(self) -> None:
        """Displays available AI templates."""
        templates = self.chat.get_templates()
        if templates is None:
            menu.alert("Error getting templates.")
            return
        if not templates.templates:
            menu.alert("Template list is empty.")
            return

        menu.iterables_show(
            ((t.name, t.description) for t in templates.templates),
            ("Name", "Description"),
            is_pasue=True,
            previous_messages=self.messages,
        )

    def show_AI_models(self) -> None:
        """Displays available AI models."""
        models_response = self.chat.get_AI_models()
        if models_response is None:
            menu.alert("Error getting models.")
            return

        if not models_response.models:
            menu.alert("AI models list is empty.")
        else:
            # Updated Schema: name
            menu.iterables_show(
                ((model.name, "") for model in models_response.models),
                ("Name", "Description"),
                is_pasue=True,
                previous_messages=self.messages,
            )

    def show_chats(self) -> None:
        """Displays a list of user chats."""
        chats = self.chat.get_chats()
        if chats is None or not chats.conversations:
            menu.alert("Chats not found")
            return

        templates = self.chat.get_templates()
        template_map = {t.id: t.name for t in templates.templates} if templates else {}

        # Updated Schema: title, ai_prompt_id
        menu.simple_iterables_show(
            tuple(
                f"{chat.title} [{template_map.get(chat.ai_prompt_id, 'Unknown')}]"
                for chat in chats.conversations
            ),
            ("Title", "Template"),
            self.messages,
            True,
        )

    def show_header(self) -> None:
        """Clears screen and shows the navigation breadcrumbs/header."""
        clear_screen()
        menu.print_message_list(self.messages)


# --- Route Definitions ---

GENERAL_ROUTES: Tuple[Tuple[str, Callable[[ConsoleCLI], None]], ...] = (
    ("Show AI models", ConsoleCLI.show_AI_models),
    ("Show templates", ConsoleCLI.show_templates),
)

UNAUTHENTICATED_ROUTES: Tuple[Tuple[str, Callable[[ConsoleCLI], None]], ...] = (
    ("Login", ConsoleCLI.login_flow),
    ("Register", ConsoleCLI.register_flow),
) + GENERAL_ROUTES

AUTHENTICATED_ROUTES: Tuple[Tuple[str, Callable[[ConsoleCLI], None]], ...] = (
    ("New chat", ConsoleCLI.create_chat_flow),
    ("Select chat", ConsoleCLI.select_chat_flow),
    ("Show chats", ConsoleCLI.show_chats),
    ("Delete chat", ConsoleCLI.delete_chat_flow),
    ("Log out", ConsoleCLI.logout),
    ("Delete user", ConsoleCLI.delete_user),
) + GENERAL_ROUTES
