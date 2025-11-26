# authentication.py
"""
Authentication module for the CLI.

Handles user login, registration, logout, and account deletion by communicating
with the backend authentication endpoints.
"""


import httpx
from starlette import status

# Custom modules
import menu
from digiliencia.configs.fastAPI.core.endpoints import LOGIN, REGISTER, USERS_ME


def login(client: httpx.Client, email: str, password: str) -> bool:
    """
    Authenticates the user and configures the client with the JWT token.

    Args:
        client (httpx.Client): The HTTP client instance.
        email (str): User email.
        password (str): User password.

    Returns:
        bool: True if login was successful, False otherwise.
    """
    payload = {"email": email, "password": password}

    try:
        response = client.post(LOGIN, json=payload)
    except httpx.RequestError as e:
        menu.alert(f"Network error during login: {e}")
        return False

    if response.status_code == status.HTTP_200_OK:
        try:
            data = response.json()
            token = data.get("access_token")
            if token:
                # Update the client headers to include the token for future requests
                client.headers["Authorization"] = f"Bearer {token}"
                return True
            else:
                menu.alert("Login failed: No access token received.")
        except ValueError:
            menu.alert("Login failed: Invalid server response.")
        return False

    elif response.status_code == status.HTTP_401_UNAUTHORIZED:
        # Don't show detailed errors for security (prevent enumeration)
        menu.alert("Incorrect email or password.", 0)
        return False

    elif response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT:
        # Validation error (e.g., invalid email format sent from CLI)
        detail = response.json().get("detail", [])
        msg = (
            detail[0].get("msg")
            if isinstance(detail, list) and detail
            else "Invalid data"
        )
        menu.alert(f"Login validation error: {msg}", 0)
        return False

    else:
        menu.alert(f"Unexpected error ({response.status_code}): {response.text}")
        return False


def register(client: httpx.Client, email: str, password: str) -> bool:
    """
    Registers a new user.

    Args:
        client (httpx.Client): The HTTP client instance.
        email (str): User email.
        password (str): User password.

    Returns:
        bool: True if registration was successful, False otherwise.
    """
    payload = {"email": email, "password": password}

    try:
        response = client.post(REGISTER, json=payload)
    except httpx.RequestError as e:
        menu.alert(f"Network error during registration: {e}")
        return False

    if response.status_code == status.HTTP_201_CREATED:
        return True

    # Handle Validation Errors (422) - e.g. Invalid email format
    if response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT:
        error_data = response.json()
        detail = error_data.get("detail", [])

        error_msg = "Invalid input data."
        if isinstance(detail, list):
            # Construct a friendly message from Pydantic errors
            for error in detail:
                field = error.get("loc", ["unknown"])[-1]
                msg = error.get("msg", "")
                if field == "email":
                    error_msg = f"Invalid email: {msg}"
                    break
                elif field == "password":
                    error_msg = f"Invalid password: {msg}"
                    break

        menu.alert(error_msg)
        return False

    # Handle Bad Request (400) - e.g. Password too short, user already exists
    if response.status_code == status.HTTP_400_BAD_REQUEST:
        error_detail = response.json().get("detail")
        # If 'detail' is a dict (fastapi-users often returns string or dict)
        reason = (
            error_detail.get("reason")
            if isinstance(error_detail, dict)
            else str(error_detail)
        )
        menu.alert(f"Registration failed: {reason}")
        return False

    menu.alert(f"Registration failed ({response.status_code}): {response.text}")
    return False


def logout(client: httpx.Client) -> bool:
    """
    Logs out the user by clearing the local token and notifying the server.

    Args:
        client (httpx.Client): The HTTP client instance.

    Returns:
        bool: True if logout was successful.
    """
    try:
        # Notify server (optional for JWT but good for logic/logging)
        response = client.post(USERS_ME)

        if response.status_code == status.HTTP_200_OK:
            client.headers.pop("Authorization", None)
            menu.alert("Logout successful.")
            return True
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            # Token was already invalid, just clear locally
            client.headers.pop("Authorization", None)
            return True

        menu.alert(f"Logout failed: {response.text}")
        return False

    except httpx.RequestError:
        # Even if network fails, we should clear the local session
        client.headers.pop("Authorization", None)
        menu.alert("Logged out locally (Server unreachable).")
        return True


def delete_user(client: httpx.Client) -> bool:
    """
    Permanently deletes the current user's account.

    Args:
        client (httpx.Client): The HTTP client instance.

    Returns:
        bool: True if deletion was successful.
    """
    try:
        response = client.delete(USERS_ME)
    except httpx.RequestError as e:
        menu.alert(f"Network error: {e}")
        return False

    if response.status_code == status.HTTP_204_NO_CONTENT:
        client.headers.pop("Authorization", None)
        menu.alert("User account deleted successfully.")
        return True

    if response.status_code == status.HTTP_401_UNAUTHORIZED:
        menu.alert("Unauthorized: Please login again.")
        return False

    menu.alert(f"User deletion failed: {response.text}")
    return False
