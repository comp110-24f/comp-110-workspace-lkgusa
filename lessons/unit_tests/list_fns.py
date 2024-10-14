"""List functions"""


def get_first(input: list[str]) -> str:
    """Returns first element of a list"""
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Removes the first element in a list"""
    input.pop(0)
    print(input)


def get_and_remove_first(input: list[str]) -> str:
    """Remove and return first element in a list"""
    first_elem: str = input[0]
    input.pop(0)  # Removes first element
    return first_elem  # Since first elem is saved in memory it can still be returned
    # after being removed from the list
