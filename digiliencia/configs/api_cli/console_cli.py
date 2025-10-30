import httpx
from starlette import status
from typing import Tuple, Callable, Dict, Optional
import uuid
import os

from digiliencia.configs.fastAPI.core.endpoints import HEALTH_PATH
import menu
import chat

import authentication


class console_cli:
    def __init__(self, url: str) -> None:
        self.messages: list[str] = ["Dilignecia CLI"]
        self.client: httpx.Client = httpx.Client(base_url=url)
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
        self.routes: Dict[
            str | uuid.UUID, Callable[[console_cli], Tuple[bool, Optional[str]]]
        ] = authenticated_routes if logged else unauthenticated_routes
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

    def login_flow(self) -> Tuple[bool, Optional[str]]:
        MAX_TRY = 3
        counter = MAX_TRY
        try:
            inputs = menu.input_menu({"email": str, "password": str},self.messages)
            while not authentication.login(
                self.client, inputs["email"], inputs["password"]
            ):
                counter -= 1
                if counter == 0:
                    return (False, "Maximum login attempts exceeded.")
                inputs = menu.input_menu(
                    {"email": str, "password": str}, "Login failed. Please try again."
                )
            self.messages.append(f"Logged as: {inputs['email']}")
            return (True, "Login successful.")
        except KeyboardInterrupt:
            return False, None

    def register_flow(self, message : Optional[str] = None) -> Tuple[bool, Optional[str]]:
        try:
            inputs = menu.input_menu(
                {"email": str, "password": str},
                self.messages,message
            )
        except KeyboardInterrupt:
            return False, None
        try:
            results = authentication.register(
                self.client, inputs["email"], inputs["password"]
            )
        except Exception as e:
            return (False, f"Registration failed with an unexpected error: {e}")
        if not results[0]:
            self.register_flow("Registration failed: " + results[2] + " Please try again.")
        if not results[1]:
            return (
                False,
                "Registration succeeded but automatic login failed. Please try to login manually.",
            )
        self.messages.append(f"Logged as: {inputs['email']}")
        return (True, "Registration and login successful.")

    def delete_user(self) -> Tuple[bool, Optional[str]]:
        return authentication.delete_user(self.client)

    def logout(self) -> Tuple[bool, Optional[str]]:
        return authentication.logout(self.client)

    def create_chat_flow(self) -> Tuple[bool, Optional[str]]:
        tittle_key = "tittle"
        tittle: str = menu.input_menu({tittle_key: str},self.messages, "Creating a chat.")[tittle_key]
        # Invert keys and values: use template name as key and UUID as value
        templates = chat.get_templates(self.client)
        template_dict: Dict[str | uuid.UUID, uuid.UUID] = {
            v[0]: uuid.UUID(str(k)) for k, v in templates.items()
        }
        template: uuid.UUID = menu.selection(template_dict, self.messages)

        success, message = chat.create_chat(self.client, tittle, template)
        if success:
            return True, "Chat created."
        return False, message

    def select_chat_flow(self) -> Tuple[bool, Optional[str]]:
        chats: Dict[uuid.UUID | str, Tuple[str, uuid.UUID]] = chat.get_chats(
            self.client
        )
        selected_chat_id: uuid.UUID = menu.selection(chats, self.messages)
        chat_messages, message = chat.get_chat(self.client,selected_chat_id)
        if chat_messages is None:
            menu.alert(message)
            return False, None
        
        menu.iterables_show(chat_messages,is_pasue=False)
        message_text: str = "Message"
        #Improvisation
        ia_model_id : uuid.UUID = list(chat.get_AI_models(self.client).keys())[0]
        while True:
            try:
                message : str = menu.input_menu({message_text: str})[message_text]
            except KeyboardInterrupt:
                break
            response, state_response = chat.ask_question(self.client,message,selected_chat_id,ia_model_id)
            if response is None:
                menu.alert(state_response)
                return False,None
            print(f"IA: {response}")

        return True, None

    def delete_chat_flow(self) -> Tuple[bool, Optional[str]]:
        chats: dict[uuid.UUID | str, Tuple[str, uuid.UUID]] = chat.get_chats(
            self.client
        )
        if not bool(chats):
            menu.alert("No chats found.")
        else:
            chat_id: uuid.UUID = menu.selection(
                {value[0]: key for key, value in chats.items()}, self.messages
            )
            if chat_id:
                success, messaje = chat.delete_chat(self.client, chat_id)
                if success:
                    menu.alert("Chat deleted")
                else:
                    menu.alert(f"Unenable delete chat. Error: {messaje}")
        return True, None

    def show_templates(self) -> Tuple[bool, Optional[str]]:
        templates: dict = chat.get_templates(self.client)
        if not bool(templates):
            menu.alert("Template list is empty.")
        else:
            menu.iterables_show(
                templates.values(), ("Name", "Description"), is_pasue=True,
                previous_messages=self.messages
            )
        return True, None

    def show_AI_models(self) -> Tuple[bool, Optional[str]]:
        models: Dict[uuid.UUID, Tuple[str]] = chat.get_AI_models(self.client)
        if not bool(models):
            menu.alert("AI models list is empty.")
        else:
            menu.iterables_show(models.values(), ("Name", "Description"), is_pasue=True,
                previous_messages=self.messages)
        return True, None

    def show_chats(self) -> Tuple[bool, Optional[str]]:
        chats: Dict[uuid.UUID | str, Tuple[str, uuid.UUID]] = chat.get_chats(
            self.client
        )
        if not bool(chats):
            menu.alert("No chats found.")
        else:
            menu.iterables_show(
                chats.values(), ("Tittle", "Template"), self.messages, True
            )
        return True, None


general_routes: Dict[
    str | uuid.UUID, Callable[[console_cli], Tuple[bool, Optional[str]]]
] = {
    "show AI models": console_cli.show_AI_models,
    "show_templates": console_cli.show_templates,
}

unauthenticated_routes: Dict[
    str | uuid.UUID, Callable[[console_cli], Tuple[bool, Optional[str]]]
] = {
    "login": console_cli.login_flow,
    "register": console_cli.register_flow,
    "show AI models": console_cli.show_AI_models,
    "show_templates": console_cli.show_templates,
} | general_routes

authenticated_routes: Dict[
    str | uuid.UUID, Callable[[console_cli], Tuple[bool, Optional[str]]]
] = {
    "New chat": console_cli.create_chat_flow,
    "Select chat": console_cli.select_chat_flow,
    "Show chats": console_cli.show_chats,
    "Delete chat": console_cli.delete_chat_flow,
    "Log out": console_cli.logout,
    "Delete user": console_cli.delete_user,
} | general_routes
