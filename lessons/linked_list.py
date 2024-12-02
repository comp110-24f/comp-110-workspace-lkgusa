"""Practice with linked lists in class 11/13."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
        """Represent a node object as a string."""
        rest: str = "?"
        # Wishful thinking: get rest of list str
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"

    # This function will print TODO whenever print(two) print(one) or print(courses)
    # Is called since there is no method called with it to override


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))
print(one)
print(courses)


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))


def last(head: Node) -> int:
    """Return the last value of a linked list."""
    if head.next is None:
        # Base case
        return head.value
    else:
        # Recursive case
        return last(head.next)


print(last(one))  # Expect two
print(last(courses))  # Expect 301

# Stack overflow indicates a recursion error!!


def recursive_range(start: int, end: int) -> Node | None:
    """Build a linked list recursively from start to end (not inclusive)"""
    # Edge case
    if start > end:
        raise ValueError("Invalid use of recursive_range")
    if start == end:
        # Base case
        return None
    else:
        # Recursive case
        # Intuition: handle first case based on specific call
        first: int = start
        # Build the rest of the list using the builder function recursively
        rest: Node | None = recursive_range(start + 1, end)
        return Node(first, rest)


a: Node | None = recursive_range(2, 8)
b: Node | None = recursive_range(110, 112)
print(a)
print(b)
