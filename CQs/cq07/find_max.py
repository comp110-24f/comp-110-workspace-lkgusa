__author__ = "730663471"


def find_and_remove_max(input: list[int]) -> int:
    max_num: int = max(input)
    if input == []:
        return -1
    for elem in input:
        if elem == max_num:
            input.pop(elem)
    return max_num
