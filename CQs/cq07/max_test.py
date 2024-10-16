from CQs.cq07.find_max import find_and_remove_max

__author__ = "730663471"


def test_find_and_remove_max_returns_correct() -> None:
    sequence: list[int] = [1, 2, 3, 4, 5]
    assert find_and_remove_max(sequence) == 5


def test_find_and_remove_max_mutates_list() -> None:
    sequence1: list[int] = [1, 7, 2, 8, 6, 8]
    find_and_remove_max(sequence1)
    assert sequence1 == [1, 7, 2, 6]


def test_find_and_remove_max_edge_case() -> None:
    sequence2: list[int] = []
    assert find_and_remove_max(sequence2) == -1
