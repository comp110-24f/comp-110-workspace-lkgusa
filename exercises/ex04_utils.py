"""Utilities of lists"""

__author__ = "730663471"


def all(items: list[int], num: int) -> bool:
    index: int = 0
    count: int = 0
    if len(items) == 0:
        # If items is an empty list, return False
        return False
    while index < len(items):
        if items[index] == num:
            count += 1
            index += 1
        else:
            index += 1
    if count == len(items):
        return True
    else:
        return False


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    largest: int = input[
        0
    ]  # The largest number is set to the first value of the list by default
    while index < len(input):
        if input[index] > largest:
            # If the value at the current index is greater than largest,
            # which is set to the first value of the list,
            # then largest will be updated to be the integer at the current index
            largest = input[index]
        index += 1
        # Even if input[index] is not greater than largest, the index is updated
        # to the next element in the list
    return largest


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    index: int = 0
    count: int = 0
    while index < len(list_1) and index < len(list_2):
        if list_1[index] == list_2[index]:
            count += 1
        index += 1
    if count == len(list_1) and count == len(list_2):
        return True
    else:
        return False


def extend(list_1: list[int], list_2: list[int]) -> None:
    index: int = 0
    while index < len(list_2):
        list_1.append(list_2[index])
        index += 1
