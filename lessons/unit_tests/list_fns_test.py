from lessons.unit_tests.list_fns import get_and_remove_first, remove_first, get_first


def test_get_first() -> None:
    desserts: list[str] = ["Cake", "Pie", "Cookie"]
    assert get_first(desserts) == "Cake"


def test_remove_first() -> None:
    """Test that remove_first returns None"""
    desserts: list[str] = ["Cake", "Pie", "Cookie"]
    assert remove_first(desserts) is None


def test_remove_first_behavior() -> None:
    """Tests that remove_first removes the first element of given list"""
    desserts: list[str] = ["Cake", "Pie", "Cookie"]
    remove_first(desserts)
    assert desserts == ["Pie", "Cookie"]


def test_get_first_edge_case() -> None:
    """Test that get_first works with an empty list"""
    input: list[str] = []
    assert get_first([]) == ""
