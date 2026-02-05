# menu.py
"""
User Interface (UI) utilities for the CLI.

This module handles console input/output, menu rendering, clearing the screen,
and capturing user choices securely.
"""

import os
import time
from typing import Any, Dict, Iterable, List, Optional, Tuple, Type


def clear_screen() -> None:
    """Clears the console screen in a cross-platform way."""
    os.system("cls" if os.name == "nt" else "clear")


def print_message_list(messages: Optional[Iterable[str]]) -> None:
    """Prints a list of context messages (breadcrumbs/logs) at the top."""
    if messages:
        print("-" * 40)
        for message in messages:
            print(f" {message}")
        print("-" * 40)


def pause(message: str = "Press Enter to continue...") -> None:
    """Pauses execution until the user presses Enter."""
    try:
        input(f"\n{message}")
    except KeyboardInterrupt:
        pass


def alert(message: str, seconds: float = 1.5, clean: bool = False) -> None:
    """
    Displays a temporary alert message.

    Args:
        message (str): The message to display.
        seconds (float): Time to wait before continuing. If 0, waits for input.
        clean (bool): If True, clears the screen before showing the alert.
    """
    if clean:
        clear_screen()

    print(f"\n[!] {message}\n")

    if seconds > 0:
        time.sleep(seconds)
    else:
        pause()


def confirm(question: str) -> bool:
    """
    Asks the user a Yes/No question.

    Returns:
        bool: True if 'y' or 'yes', False otherwise.
    """
    while True:
        try:
            response = input(f"{question} (y/n): ").strip().lower()
            if response in ("y", "yes"):
                return True
            if response in ("n", "no"):
                return False
        except KeyboardInterrupt:
            return False


def input_menu(
    input_schema: Dict[str, Type],
    previous_messages: Optional[Iterable[str]] = None,
    header_message: Optional[str] = None,
    clean: bool = True,
) -> Dict[str, Any]:
    """
    Prompts the user for multiple inputs based on a schema.

    Args:
        input_schema (dict): Key name and expected Type (e.g. {'age': int}).
        previous_messages (list): Context messages to show.
        header_message (str): Specific instruction for this input block.

    Returns:
        dict: The captured inputs with correct types.
    """
    if clean:
        clear_screen()
    print_message_list(previous_messages)

    if header_message:
        print(f"{header_message}\n")

    inputs: Dict[str, Any] = {}

    for key, type_func in input_schema.items():
        valid_input = False
        while not valid_input:
            try:
                raw_value = input(f"Enter {key}: ").strip()

                # Allow exiting current flow on empty input if desired,
                # or enforce strictness. Here we verify types.
                if not raw_value:
                    print("  Value cannot be empty.")
                    continue

                # Convert to expected type
                value = type_func(raw_value)
                inputs[key] = value
                valid_input = True

            except ValueError:
                print(f"  Invalid format for {key}. Expected {type_func.__name__}.")
            except KeyboardInterrupt:
                raise  # Let the caller handle Ctrl+C

    return inputs


def _print_table_row(row_items: Any, is_header: bool = False) -> None:
    """Helper to print aligned columns."""
    if isinstance(row_items, str):
        print(row_items)
        if is_header:
            print("-" * len(row_items))
        return

    # Simple tab separation for CLI
    row_str = "\t".join(str(item) for item in row_items)
    print(row_str)
    if is_header:
        print("-" * len(row_str.expandtabs()))


def iterables_show(
    entries: Iterable[Iterable[Any]],
    header: Optional[Iterable[str]] = None,
    previous_messages: Optional[List[str]] = None,
    is_pasue: bool = False,
    pause_message: Optional[str] = None,
    clean: bool = True,
) -> None:
    """
    Displays a table of data (rows and columns).
    Used for showing lists of templates, models, etc.
    """
    if clean:
        clear_screen()
    print_message_list(previous_messages)

    if header:
        _print_table_row(header, is_header=True)

    for i, row in enumerate(entries, start=1):
        # Prepend index for readability, though this isn't a selection menu
        print(f"{i}. ", end="")
        _print_table_row(row)

    if is_pasue:
        pause(pause_message or "Press Enter to return...")


def simple_iterables_show(
    entries: Iterable[Any],
    header: Optional[Iterable[str]] = None,
    previous_messages: Optional[List[str]] = None,
    is_pasue: bool = False,
) -> None:
    """
    Displays a simple list of items.
    """
    clear_screen()
    print_message_list(previous_messages)

    if header:
        _print_table_row(header, is_header=True)

    for i, item in enumerate(entries, start=1):
        print(f"{i}. {item}")

    if is_pasue:
        pause()


def selection(
    options: Tuple[Tuple[str, Any], ...],
    previous_messages: Optional[Iterable[str]] = None,
    error_message: Optional[str] = None,
) -> Any:
    """
    Displays a numbered menu and captures the user's choice.

    Args:
        options: A tuple of (Display Name, Return Value).
        previous_messages: Context headers.
        error_message: Message to display if the previous attempt failed.

    Returns:
        The value associated with the selected option, or None on cancel.
    """
    while True:
        clear_screen()
        print_message_list(previous_messages)

        print("\nSelect an option:")
        for idx, (label, _) in enumerate(options, start=1):
            print(f"  {idx}. {label}")

        print("\n  0. Cancel / Back")

        if error_message:
            print(f"\n[!] {error_message}")
            error_message = None  # Reset after showing once

        try:
            user_input = input("\n> ")
            choice_idx = int(user_input)

            if choice_idx == 0:
                return None

            if 1 <= choice_idx <= len(options):
                return options[choice_idx - 1][1]
            else:
                error_message = "Option out of range."

        except ValueError:
            error_message = "Invalid input. Please enter a number."
        except KeyboardInterrupt:
            return None
