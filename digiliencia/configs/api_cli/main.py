import argparse
import socket
import httpx
from starlette import status
from digiliencia.configs.fastAPI.core.endpoints import HEALTH_PATH

from menu import menu
from settings import unauthenticated_routes, authenticated_routes


def address_format_validation(ip_port):
    try:
        ip, port = ip_port.split(":")

        socket.inet_aton(ip)

        port = int(port)
        if port < 1 or port > 65535:
            raise ValueError(f"Invalid port number ({port}).")

        return ip, port
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid format. {str(e)}")
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Invalid input. Error: {str(e)}")


def initial_menu_flow(client: httpx.Client):
    is_logged_in = False
    not_exist = True
    message = None
    while not_exist:
        not_exist, message = menu(
            client,
            unauthenticated_routes if not is_logged_in else authenticated_routes,
            message,
        )
        is_logged_in = client.headers.get("Authorization") is not None

    print("Exiting application.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="CLI for Digiliencia API configuration management."
    )

    parser.add_argument(
        "--ip_port",
        type=address_format_validation,
        help="IP address and port in format IP:port",
        default="localhost:8080",
    )

    args = parser.parse_args()

    ip, port = args.ip_port
    URL = f"http://{ip}:{port}/api"
    print(f"Configured API URL: {URL}")

    try:
        client = httpx.Client(base_url=URL, timeout=5)
        response = client.get(HEALTH_PATH)
        if (
            response.status_code == status.HTTP_200_OK
            and response.json().get("status") == "ok"
        ):
            initial_menu_flow(client)
        else:
            print("Could not connect to the API. Error:", response.json)
    except httpx.HTTPError as e:
        print("Error connecting to the API:", str(e))
