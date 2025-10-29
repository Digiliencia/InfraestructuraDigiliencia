import httpx
from typing import Tuple, Optional

import auth
import menu


def login_flow(client: httpx.Client) -> Tuple[bool, Optional[str]]:
    MAX_TRY = 3
    counter = MAX_TRY
    try:
        inputs = menu.input_menu({"email": str, "password": str})
        while not auth.login(client, inputs["email"], inputs["password"]):
            counter -= 1
            if counter == 0:
                return (False, "Maximum login attempts exceeded.")
            inputs = menu.input_menu(
                {"email": str, "password": str}, "Login failed. Please try again."
            )
        return (True, "Login successful.")
    except KeyboardInterrupt:
        return False, None


def register_flow(
    client: httpx.Client, previous_message: Optional[str] = None
) -> Tuple[bool, str]:
    try:
        inputs = menu.input_menu({"email": str, "password": str}, previous_message)
    except KeyboardInterrupt:
        return False, None
    try:
        results = auth.register(client, inputs["email"], inputs["password"])
    except Exception as e:
        return (False, f"Registration failed with an unexpected error: {e}")
    if not results[0]:
        return register_flow(
            client, "Registration failed: " + results[2] + " Please try again."
        )
    if not results[1]:
        return (
            False,
            "Registration succeeded but automatic login failed. Please try to login manually.",
        )
    return (True, "Registration and login successful.")
