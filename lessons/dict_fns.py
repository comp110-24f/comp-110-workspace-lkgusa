"""Practice with writing dictionary functions before Quiz 03."""


def value_exists(test_dict: dict[str, int], test_int: int) -> bool:
    """Checks if test_int is in test_dict."""
    count: int = 0
    for key in test_dict:
        val = test_dict[key]
        if val == test_int:
            count += 1
    if count > 0:
        return True
    else:
        return False


def plus_or_minus_n(inp: dict[str, int], n: int) -> None:
    """Depending on whether inp value is even or odd, add or subtract n"""
    for key in inp:
        val = inp[key]
        if val % 2 == 0:
            val += n
        else:
            val -= n


def free_biscuits(test_dict: dict[str, list[int]]) -> dict[str, bool]:
    """Returns dictionary of basketball games where free biscuits were won or not"""
    bisc_games: dict[str, bool] = {}
    for key in test_dict:
        val = test_dict[key]
        if sum(val) >= 100:
            bisc_games[key] = True
        else:
            bisc_games[key] = False
    return bisc_games


def max_key(input: dict[str, list[int]]) -> str:
    max_key: str = ""
    max_val_sum: int = 0

    for key in input:
        val_sum: int = 0
        for value in input[key]:
            val_sum += value
        if val_sum > max_val_sum:
            max_val_sum = val_sum
            max_key = key
    return max_key


def merge_lists(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    empty_dict: dict[str, int] = {}
    if len(str_list) != len(int_list):
        return empty_dict

    merged_dict: dict[str, int] = {}
    index: int = 0
    for elem in str_list:
        merged_dict[elem] = int_list[index]
        index += 1
    return merged_dict
