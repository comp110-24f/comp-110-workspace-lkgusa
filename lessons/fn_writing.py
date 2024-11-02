def odd_and_even(input: list[int]) -> list[int]:
    new_list: list[int] = []
    idx: int = 0
    while idx < len(input):
        if input[idx] % 2 != 0 and idx % 2 == 0:
            new_list.append(input[idx])
            idx += 1
        else:
            idx += 1
    return new_list


def short_words(input: list[str]) -> list[str]:
    """Returns list of words that are shorter than 5 characters."""
    new_list: list[str] = []
    for word in input:
        if len(word) < 5:
            new_list.append(word)
        else:
            print(f"{word} was too long")
    return new_list


def multiples(input: list[int]) -> list[bool]:
    bool_list: list[bool] = []
    idx: int = 0
    while idx < len(input):
        if idx == 0:
            if input[idx] % input[(len(input) - 1)] == 0:
                bool_list.append(True)
            idx += 1
        if input[idx] % input[idx - 1] == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
        idx += 1
    return bool_list


def value_exists(test_dict: dict[str, int], test_val: int) -> bool:
    for val in test_dict:
        if test_dict[val] == test_val:
            return True
    return False


