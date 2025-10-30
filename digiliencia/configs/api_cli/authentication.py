import httpx
from starlette import status
from digiliencia.configs.fastAPI.core.endpoints import LOGIN, REGISTER, USERS_ME
from typing import Tuple, Optional


def login(client: httpx.Client, email: str, password: str) -> bool:
    response = client.post(LOGIN, json={"email": email, "password": password})

    if response.status_code == 200:
        token = response.json()["access_token"]
        client.headers.update({"Authorization": f"Bearer {token}"})
        return True
    if (
        response.status_code == status.HTTP_401_UNAUTHORIZED
        or response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
    ):
        return False
    raise Exception(
        f"Login failed with status code {response.status_code}: {response.text}"
    )


def register(client: httpx.Client, email: str, password: str) -> tuple[bool, bool, str]:
    response = client.post(REGISTER, json={"email": email, "password": password})

    if response.status_code == status.HTTP_201_CREATED:
        return (True, login(client, email, password), "")
    if response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT:
        error_detail = response.json()
        if "detail" in error_detail:
            for error in error_detail["detail"]:
                if "email" in error["loc"]:
                    return (
                        False,
                        False,
                        f"Enter a valid email address:\n{error['msg']}",
                    )
    if response.status_code == status.HTTP_400_BAD_REQUEST:
        error_detail = response.json()["detail"]
        return (False, False, error_detail["reason"])
    raise Exception(
        f"Registration failed with status code {response.status_code}: {response.text}"
    )


## It do not logout, delete the user from the server
def logout(client: httpx.Client) -> Tuple[bool, Optional[str]]:
    response = client.delete(USERS_ME)
    if response.status_code == status.HTTP_204_NO_CONTENT:
        client.headers.pop("Authorization", None)
        return (True, "Logout successful.")
    return (False, f"Logout failed: {response.text}")


def delete_user(client: httpx.Client) -> Tuple[bool, Optional[str]]:
    response = client.delete(USERS_ME)
    if response.status_code == status.HTTP_204_NO_CONTENT:
        client.headers.pop("Authorization", None)
        return (True, "User deleted successfully.")
    return (False, f"User deletion failed: {response.text}")
