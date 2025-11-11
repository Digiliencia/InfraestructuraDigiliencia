import argparse
import socket

import console_cli


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

    interface: console_cli.console_cli = console_cli.console_cli(URL)
    try:
        interface.initial_menu_flow()
    except ConnectionRefusedError:
        print("Connection refused.")
