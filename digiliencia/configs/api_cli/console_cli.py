import httpx
from starlette import status
from typing import Tuple, Callable, Optional
import uuid
import os

import digiliencia.configs.fastAPI.schemas.chat as chat_schema

from digiliencia.configs.fastAPI.core.endpoints import HEALTH_PATH
import menu
from chat import Chat

import authentication


class console_cli:
    def __init__(self, url: str) -> None:
        self.messages: list[str] = ["Dilignecia CLI"]
        self.client: httpx.Client = httpx.Client(base_url=url)
        self.chat: Chat = Chat(self.client)
        self.alert_time: float = 0.7
        try:
            response = self.client.get(HEALTH_PATH)
            if (
                response.status_code != status.HTTP_200_OK
                or response.json().get("status") != "ok"
            ):
                print("Could not connect to the API. Error:", response.json)
        except httpx.HTTPError as e:
            print("Error connecting to the API:", str(e))

    def is_logged_in(self) -> bool:
        logged: bool = self.client.headers.get("Authorization") is not None
        self.routes: Tuple[Tuple[str, Callable[[console_cli], None]], ...] = (
            authenticated_routes if logged else unauthenticated_routes
        )
        return logged

    def initial_menu_flow(self) -> None:
        while True:
            os.system("clear")
            self.is_logged_in()
            selectioned: Callable[[console_cli], Tuple[bool, str]] = menu.selection(
                self.routes,
                self.messages,
            )
            os.system("clear")
            if selectioned is None:
                break
            selectioned(self)
        if self.is_logged_in():
            self.logout()
        print("Exiting application.")

    def login_flow(self) -> None:
        MAX_TRY = 3
        counter = MAX_TRY
        try:
            inputs = menu.input_menu({"email": str, "password": str}, self.messages)
            while not authentication.login(
                self.client, inputs["email"], inputs["password"]
            ):
                counter -= 1
                if counter == 0:
                    menu.alert("Maximum login attempts exceeded.", self.alert_time * 2)
                    return
                inputs = menu.input_menu({"email": str, "password": str})
            self.messages.append(f"Logged as: {inputs['email']}")
            menu.alert("Login successful.", self.alert_time)
        except KeyboardInterrupt:
            return

    def register_flow(self, message: Optional[str] = None) -> None:
        try:
            inputs = menu.input_menu(
                {"email": str, "password": str}, self.messages, message
            )
        except KeyboardInterrupt:
            return

        if authentication.register(self.client, inputs["email"], inputs["password"]):
            if not authentication.login(
                self.client, inputs["email"], inputs["password"]
            ):
                menu.alert(
                    "Registration succeeded but automatic login failed. Please try to login manually.",
                    self.alert_time,
                )
        else:
            return
        self.messages.append(f"Logged as: {inputs['email']}")
        menu.alert("Registration and login successful.", self.alert_time)

    def delete_user(self) -> None:
        authentication.delete_user(self.client)

    def logout(self) -> None:
        if authentication.logout(self.client):
            self.messages.pop()

    def create_chat_flow(self) -> None:
        tittle_key = "tittle"
        tittle: str = menu.input_menu(
            {tittle_key: str}, self.messages, "Creating a chat."
        )[tittle_key]
        templates = self.chat.get_templates()
        if templates is None:
            menu.alert("Error getting templates.")
            return

        template: uuid.UUID = menu.selection(
            tuple(
                (
                    f"{template.template_name} {template.template_description}",
                    str(template.idTemplate),
                )
                for template in templates.templates
            ),
            self.messages,
        )

        if self.chat.create_chat(tittle, template):
            menu.alert("Chat created.")

    def select_chat_flow(self) -> None:
        chats: Optional[chat_schema.ConversationSummaries] = self.chat.get_chats()
        if chats is None or not bool(chats.conversations):
            menu.alert("Chats not found")
            return
        templates: Optional[chat_schema.Templates] = self.chat.get_templates()
        selected_chat_id: uuid.UUID = menu.selection(
            tuple(
                (
                    f"{chat.tittle} {templates.templates[0].template_name if templates is not None else ''}",
                    str(chat.idChat),
                )
                for chat in chats.conversations
            ),
            self.messages,
        )
        if selected_chat_id is None:
            return False, None
        chat_messages, message = self.chat.get_chat(selected_chat_id)
        if chat_messages is None:
            menu.alert(message)
            return

        self.conversation_flow(chat_messages, selected_chat_id)

    def conversation_flow(
        self, chat_messages: list[str], selected_chat_id: uuid.UUID
    ) -> None:
        self.show_header()
        menu.iterables_show(chat_messages, is_pasue=False)
        message_text: str = "Message"
        # Improvisation
        ia_model_id = self.chat.get_AI_models()
        if ia_model_id is None:
            menu.alert("AI model not found")
            return
        while True:
            try:
                message: str = menu.input_menu({message_text: str})[message_text]
            except KeyboardInterrupt:
                break
            response, state_response = self.chat.ask_question(
                message, selected_chat_id, ia_model_id.models[0].idModel
            )
            if response is None:
                menu.alert(state_response)
                return
            print(f"IA: {response}")

    def delete_chat_flow(self) -> None:
        chats: Optional[chat_schema.ConversationSummaries] = self.chat.get_chats()
        if chats is None or not bool(chats.conversations):
            menu.alert("Chats not found")
        else:
            templates = self.chat.get_templates()
            selected_chat: chat_schema.ConversationSummary = menu.selection(
                tuple(
                    (
                        f"{chat.tittle} {templates.templates[0].idTemplate if templates is not None else ''}",
                        chat,
                    )
                    for chat in chats.conversations
                ),
                self.messages,
            )
            if selected_chat and self.chat.delete_chat(selected_chat.idChat):
                menu.alert(f"Chat {selected_chat.tittle} deleted", self.alert_time)

    def show_templates(self) -> None:
        templates = self.chat.get_templates()
        if templates is None:
            menu.alert("Error getting templates.")
            return
        if not bool(templates):
            menu.alert("Template list is empty.")
            return

        menu.iterables_show(
            (
                (template.template_name, template.template_description)
                for template in templates.templates
            ),
            ("Name", "Description"),
            is_pasue=True,
            previous_messages=self.messages,
        )

    def show_AI_models(self) -> None:
        models: Optional[chat_schema.Models] = self.chat.get_AI_models()
        if models is None:
            menu.alert("Error getting models.")
            return
        if not bool(models):
            menu.alert("AI models list is empty.")
        else:
            menu.iterables_show(  # Description of model not implemented
                ((model.model_name, "") for model in models.models),
                ("Name", "Description"),
                is_pasue=True,
                previous_messages=self.messages,
            )

    def show_chats(self) -> None:
        chats: Optional[chat_schema.ConversationSummaries] = self.chat.get_chats()
        if chats is None or not bool(chats.conversations):
            menu.alert("Chats not found")
        else:
            templates = self.chat.get_templates()
            menu.simple_iterables_show(
                tuple(
                    f"{chat.tittle} {next((template.template_name for template in templates.templates if template.idTemplate == chat.template), '') if templates is not None else ''}"
                    for chat in chats.conversations
                ),
                ("Tittle", "Template"),
                self.messages,
                True,
            )

    def show_header(self) -> None:
        os.system("clear")
        menu.print_message_list(self.messages)


general_routes: Tuple[Tuple[str, Callable[[console_cli], None]], ...] = (
    ("show AI models", console_cli.show_AI_models),
    ("show_templates", console_cli.show_templates),
)

unauthenticated_routes: Tuple[Tuple[str, Callable[[console_cli], None]], ...] = (
    ("login", console_cli.login_flow),
    ("register", console_cli.register_flow),
) + general_routes

authenticated_routes: Tuple[Tuple[str, Callable[[console_cli], None]], ...] = (
    ("New chat", console_cli.create_chat_flow),
    ("Select chat", console_cli.select_chat_flow),
    ("Show chats", console_cli.show_chats),
    ("Delete chat", console_cli.delete_chat_flow),
    ("Log out", console_cli.logout),
    ("Delete user", console_cli.delete_user),
) + general_routes
