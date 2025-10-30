import os
from typing import Type, Callable, Iterable, Optional, Any
import uuid


def input_menu(
    input_dict: dict[str, Type], previous_message: Optional[str] = None
) -> dict[str, Any]:
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


def dict_show(
    entries: dict[str, str],
    header: Optional[Iterable[str]] = None,
    previous_message: Optional[str] = None,
    is_pasue: bool = False,
    pause_message: Optional[str] = None,
    is_selection: bool = False,
) -> None:
    print(previous_message)
    if header:
        for head in header:
            print(f"{head}\t")
    for position, (key, value) in enumerate(entries.items(), start=1):
        print(f"{position if is_selection else ''}- {key}:\t{value}")
    if is_pasue:
        pause(pause_message)


def iterables_show(
    entries: Iterable[Iterable[str | uuid.UUID]],
    header: Optional[Iterable[str]] = None,
    previous_message: Optional[str] = None,
    is_pasue: bool = False,
    pause_message: Optional[str] = None,
    is_selection: bool = False,
) -> None:
    if previous_message is not None:
        print(previous_message)
    if header:
        for head in header:
            print(f"{head}\t", end="")
        print()
    for value in entries:
        first: bool = True
        for position, value_in_value in enumerate(value, start=1):
            if first:
                print(f"{position if is_selection else ''}- {value_in_value}", end="")
                first = False
            else:
                print(f"\t{value_in_value}", end="")
        print()
    if is_pasue:
        pause(pause_message)


def simple_iterables_show(
    entries: Iterable[str | uuid.UUID],
    header: Optional[Iterable[str]] = None,
    previous_message: Optional[str] = None,
    is_pasue: bool = False,
    pause_message: Optional[str] = None,
    is_selection: bool = False,
) -> None:
    if previous_message is not None:
        print(previous_message)
    if header:
        for head in header:
            print(f"{head}\t", end="")
        print()
    for position, value in enumerate(entries, start=1):
        print(f"{position if is_selection else ''}- {value}")
    if is_pasue:
        pause(pause_message)


def pause(message: Optional[str] = None) -> None:
    if message is None:
        message = "Press any key to continue"
    input(message)


def alert(message: str):
    print(f"{message}\n")
    pause()


def show_selection(
    routes: Iterable[str | uuid.UUID | Iterable[str | uuid.UUID]],
    header: Optional[Iterable[str]] = None,
    previous_message: Optional[str] = None,
    is_pasue: bool = False,
    pause_message: Optional[str] = None,
) -> None:
    print("Select an option:")
    selection_function: Callable[
        [
            Iterable[Iterable[str | uuid.UUID]],
            Optional[Iterable[str]],
            Optional[str],
            bool,
            Optional[str],
            Optional[bool],
        ],
        None,
    ]
    if routes is dict[str | uuid.UUID, str]:
        selection_function = dict_show
    elif routes is Iterable[Iterable[str | uuid.UUID]]:
        selection_function = iterables_show
    elif routes is Iterable[str | uuid.UUID]:
        selection_function = simple_iterables_show
    else:  # I try it
        selection_function = simple_iterables_show
    try:
        selection_function(
            routes, header, previous_message, is_pasue, pause_message, True
        )
    except Exception as e:
        raise Exception(f"Not implemented yet: {type(routes)}. {e}")


def selection(
    router: dict[str | uuid.UUID, Any],
    previous_message: Optional[str] = None,
) -> Any:
    while True:
        os.system("clear")
        if previous_message:
            print(previous_message)
        show_selection(
            list(router.keys()),
        )
        try:
            opcion = int(input("Enter option number: "))
            if opcion == 0:  # To write fewer
                raise IndexError
            opcion = list(router.keys())[opcion - 1]
            if opcion in router:
                return router[opcion]
            else:
                return selection(router, "Incorrect option.")
        except ValueError:
            return selection(router, "Invalid input. Please enter a number.")
        except IndexError:
            return selection(router, "The option number is out of range.")
        except KeyboardInterrupt:
            return None
