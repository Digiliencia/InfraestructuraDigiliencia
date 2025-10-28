import httpx
import os
from typing import Type, Tuple, Callable


def input_menu(
    input_dict: dict[str, Type], previous_message: str = ""
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


def menu(
    client: httpx.Client,
    router: dict[str, Callable[[httpx.Client], Tuple[bool, str]]],
    previous_message: str = "",
) -> Tuple[bool, str]:
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
