# main.py
"""
Entry point for the Digiliencia CLI application.

This script parses command-line arguments to configure the connection
to the backend API and initializes the console interface.
"""

import argparse
import sys
from typing import Tuple

# Import the refactored controller
import console_cli


def validate_host_port(value: str) -> Tuple[str, int]:
    """
    Validates that the input string follows the 'host:port' format.

    This validator accepts both IP addresses and hostnames (e.g., 'localhost').

    Args:
        value (str): The input string from the command line.

    Returns:
        Tuple[str, int]: A tuple containing the host (str) and port (int).

    Raises:
        argparse.ArgumentTypeError: If the format is invalid or the port is out of range.
    """
    try:
        if ":" not in value:
            raise ValueError(
                "Missing port. Format must be 'host:port' (e.g. localhost:8080)."
            )

        host, port_str = value.split(":", 1)

        if not host:
            raise ValueError("Host cannot be empty.")

        port = int(port_str)
        if port < 1 or port > 65535:
            raise ValueError(f"Port {port} is out of range (1-65535).")

        return host, port

    except ValueError as e:
        raise argparse.ArgumentTypeError(f"Invalid format: {e}")
    except Exception as e:
        raise argparse.ArgumentTypeError(f"Unexpected error validating input: {e}")


def main() -> None:
    """
    Main execution function.

    Parses arguments, constructs the API URL, and starts the CLI interface loop.
    """
    parser = argparse.ArgumentParser(
        description="CLI for Digiliencia API configuration and management."
    )

    parser.add_argument(
        "--address",
        type=validate_host_port,
        help="API address in format 'host:port' (e.g., localhost:8080)",
        default="localhost:8080",
        dest="host_port",
    )

    parser.add_argument(
        "--protocol",
        choices=["http", "https"],
        default="http",
        help="Protocol to use for the connection (default: http).",
    )

    args = parser.parse_args()

    host, port = args.host_port

    # Construct the base URL.
    # Note: We assume the API is mounted at /api based on core/endpoints.py
    api_url = f"{args.protocol}://{host}:{port}/api"

    print("-" * 50)
    print("[*] Digiliencia CLI Wrapper")
    print(f"[*] Target API: {api_url}")
    print("-" * 50)

    try:
        interface = console_cli.ConsoleCLI(api_url)

        # Start the main interaction loop
        interface.initial_menu_flow()

    except KeyboardInterrupt:
        print("\n\n[*] Exiting application. Goodbye!")
        sys.exit(0)
    except Exception as e:
        # This catches unexpected crashes that aren't handled inside ConsoleCLI
        print(f"\n[!] Critical Error during initialization: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
