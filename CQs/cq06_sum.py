"""Summing the elements of a list using different loops"""

__author__ = "730663471"


def w_sum(vals: list[float]) -> float:
    index = 0
    total = 0.0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


# print(w_sum([1.1, 0.9, 1.0])
# print(w_sum([]))


def f_sum(vals: list[float]) -> float:
    total = 0.0
    for values in vals:
        total += values
    return total


# print(f_sum([1.1, 0.9, 1.0])
# print(f_sum([]))


def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for values in range(0, len(vals)):
        # It turns out that here, total += values does not work like it does without using range(),
        # you actually have to specify to add the value at the index of vals the function is at currently in order for total to be updated after each element in the list
        # This is because total += values iterates over the numbers that range creates, not the actual elements in vals, and ends up adding the integers from range to total
        # In order to specify the loop to iterate over the vals elements, you need to say total += vals[values] to tell python to add each element in the vals list to total as it progresses as many times as are in range(0, len(vals))
        total += vals[values]
    return total


# print(f_range_sum([2.0, 2.0, 3.0]))
