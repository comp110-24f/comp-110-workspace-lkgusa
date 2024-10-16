__author__ = "730663471"


def find_and_remove_max(input: list[int]) -> int:
    max_num: int = 0
    index = 0

    if input == []:
        return -1

    while index < len(input):
        # Checks if each list value is larger than last,
        # should find the max number in the list
        if input[index] > max_num:
            max_num = input[index]
            index += 1
        else:
            index += 1

    index = 0
    # Resets index number because it was at the last value before
    while index < len(input):
        if input[index] == max_num:
            input.pop(index)  # .pop(input[index]) did not work because
            # pop only understands INDEX values not the values of the list
        else:
            index += 1

    return max_num
