from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_new_list() -> None:
    """Tests whether only_evens does only put even numbers in new list"""
    pi: list[int] = [3, 1, 4]
    assert only_evens(pi) == [4]


def test_only_evens_no_mutation() -> None:
    """Tests whether only_evens doesn't mutate original list"""
    pi: list[int] = [3, 1, 4]
    only_evens(pi)
    assert pi == [3, 1, 4]


def test_only_evens_odds_only() -> None:
    """Tests whether only_evens will return empty list if only odd numbers are given"""
    odds: list[int] = [1, 3, 5]
    assert only_evens(odds) == []


def test_sub_start_gtet_list() -> None:
    """Tests whether sub returns empty new list when start and end aren't in range"""
    e: list[int] = [2, 7, 1]
    assert sub(e, 9, -1) == []


def test_sub_correct_range() -> None:
    """Tests whether sub will return a list in the correct range"""
    e: list[int] = [2, 7, 1]
    assert sub(e, 0, 2) == [2, 7]


def test_sub_no_mutation() -> None:
    """Tests that sub will not modify the original list"""
    e: list[int] = [2, 7, 1]
    assert sub(e, 0, 1) == [2]


def test_add_at_index_edge_case() -> None:
    """Tests that add_at_index skips while loop since loc == len(input)"""
    tau: list[int] = [6, 2, 8]
    add_at_index(tau, 3, 3)  # Since add_at_index returns none you can't assert
    # that add_at_index(tau, 3, 3) == [6, 2, 8, 3] because that means
    # the test case will check that add_at_index returns that list when it returns none
    assert tau == [6, 2, 8, 3]


def test_add_at_index_regular() -> None:
    """Tests that add_at_index will modify input correctly"""
    evens: list[int] = [4, 8, 12]
    add_at_index(evens, 6, 1)
    assert evens == [4, 6, 8, 12]


def test_add_at_index_mutation() -> None:
    """Tests that add_at_index will mutate original list"""
    favorites: list[int] = [11, 31, 666]
    add_at_index(favorites, 777, 1)
    assert favorites != [11, 31, 666]
