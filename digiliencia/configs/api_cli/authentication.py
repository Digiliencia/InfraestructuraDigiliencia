import httpx
from starlette import status
from digiliencia.configs.fastAPI.core.endpoints import LOGIN, REGISTER, USERS_ME

import menu


def login(client: httpx.Client, email: str, password: str) -> bool:
    response = client.post(LOGIN, json={"email": email, "password": password})

    if response.status_code == 200:
        token = response.json()["access_token"]
        client.headers.update({"Authorization": f"Bearer {token}"})
        return True
    if response.status_code == status.HTTP_401_UNAUTHORIZED:
        menu.alert("Incorrect email or password.", 0)
        return False
    if response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT:
        menu.alert(f"Login failed: {response.json()['detail'][0]['msg']}", 0)
        return False
    menu.alert(f"Unexpected error: {response.text}")
    return False


def register(client: httpx.Client, email: str, password: str) -> bool:
    response = client.post(REGISTER, json={"email": email, "password": password})

    if response.status_code == status.HTTP_201_CREATED:
        return True
    if response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT:
        error_detail = response.json()
        if "detail" in error_detail:
            for error in error_detail["detail"]:
                if "email" in error["loc"]:
                    menu.alert(f"Enter a valid email address:\n{error['msg']}")
                    return False
    if response.status_code == status.HTTP_400_BAD_REQUEST:
        error_detail = response.json()["detail"]
        menu.alert(error_detail["reason"])
    else:
        menu.alert(
            f"Registration failed with status code {response.status_code}: {response.text}"
        )
    return False


## It do not logout, delete the user from the server
def logout(client: httpx.Client) -> bool:
    response = client.post(USERS_ME)
    if response.status_code == status.HTTP_200_OK:
        client.headers.pop("Authorization", None)
        menu.alert("Logout successful.")
        return True
    menu.alert(f"Logout failed: {response.text}")
    return False


def delete_user(client: httpx.Client) -> bool:
    response = client.delete(USERS_ME)
    if response.status_code == status.HTTP_204_NO_CONTENT:
        client.headers.pop("Authorization", None)
        menu.alert("User deleted successfully.")
        return True
    menu.alert(f"User deletion failed: {response.text}")
    return False
