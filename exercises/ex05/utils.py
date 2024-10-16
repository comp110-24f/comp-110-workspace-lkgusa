"""Continuing to build list utility functions"""

__author__ = "730663471"


def only_evens(input: list[int]) -> list[int]:
    """Given list of numbers, makes new list with only the evens from original list"""
    new_list: list[int] = []
    for value in range(0, len(input)):
        if input[value] % 2 == 0:  # Mod 2 here checks whether the number is even
            new_list.append(input[value])
    return new_list


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Given number list, makes new list of only numbers in given (start, end) range"""
    new_list: list[int] = []
    if len(input) == 0:
        return new_list

    if (start >= len(input)) or (end <= 0):
        return new_list

    if start < 0:
        start = 0

    if end > len(input):
        end = len(input)

    for value in range(start, end):
        new_list.append(input[value])

    return new_list


def add_at_index(input: list[int], add: int, loc: int) -> None:
    """Given int list, int to add, and location to add, inserts add at loc in list"""
    if loc < 0 or loc > len(input):
        raise IndexError("Index is out of bounds for the input list")

    if loc == len(input):  # This would be an edge case, directly append add to input
        input.append(add)
    else:
        input.append(input[len(input) - 1])
        # Adds value to end of input so values can be shifted right

    i: int = len(input) - 2
    while i > loc:
        # Loop shifts elements to the right, to make room for add at loc
        input[i] = input[i - 1]
        i -= 1
    input[loc] = add
