import httpx
import os
from typing import Type, Tuple, Callable, Iterable, Optional


def input_menu(
    input_dict: dict[str, Type], previous_message: Optional[str] = None
) -> dict[str, any]:
    os.system("clear")
    if previous_message:
        print(previous_message)
    inputs = dict[str, any]()
    for key, value in input_dict.items():
        while inputs.get(key) is None:
            try:
                inputs[key] = value(input(f"Introduce {key}: "))
            except Exception as e:
                print(f"Error reading input for {key}: {e}")
    return inputs


def show_menu(routes: dict):
    print(f"Select an option from menu (0 - {len(routes)}):\n")
    print("  0: Exit")
    for number, key in enumerate(routes.keys(), start=1):
        print(f"  {number}: {key}")
    print()


def dict_show(
    entries: dict[str, str],
    header: Optional[Iterable[str]] = None,
    previous_message: Optional[str] = None,
    is_pasue: bool = False,
    pause_message: Optional[str] = None,
) -> None:
    os.system("clear")
    print(previous_message)
    if header:
        for head in header:
            print(f"{head}\t")
    for key, value in entries.items():
        print(f"- {key}:\t{value}")
    if is_pasue:
        pause(pause_message)


def iterables_show(
    entries: Iterable[Iterable[str]],
    header: Optional[Iterable[str]] = None,
    previous_message: Optional[str] = None,
    is_pasue: bool = False,
    pause_message: Optional[str] = None,
) -> None:
    os.system("clear")
    if not previous_message is None:
        print(previous_message)
    if header:
        for head in header:
            print(f"{head}\t", end="")
    print()
    for value in entries:
        first: bool = True
        for value_in_value in value:
            if first:
                print(f"- {value_in_value}", end="")
                first = False
            else:
                print(f"\t{value_in_value}", end="")
        print()
    if is_pasue:
        pause(pause_message)


def pause(message: Optional[str] = None) -> None:
    if message is None:
        message = "Press any key to continue"
    input(message)


def alert(message: str):
    print(f"{message}\n")
    pause()


def menu(
    client: httpx.Client,
    router: dict[str, Callable[[httpx.Client], Tuple[bool, str]]],
    previous_message: Optional[str] = None,
) -> Tuple[bool, Optional[str]]:
    while True:
        os.system("clear")
        if previous_message:
            print(previous_message)
        show_menu(router)
        try:
            opcion = int(input("Enter option number: "))
            if opcion == 0:
                return False, "Exiting menu."
            opcion = list(router.keys())[opcion - 1]
            if opcion in router:
                return True, router[opcion](client)[1]
            else:
                return menu(client, router, "Incorrect option.")
        except ValueError:
            return menu(client, router, "Invalid input. Please enter a number.")
        except IndexError:
            return menu(client, router, "The option number is out of range.")
        except KeyboardInterrupt:
            return False, ""
