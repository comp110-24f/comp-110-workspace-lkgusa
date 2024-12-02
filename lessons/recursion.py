"""Recursive class and function calls from class 11/11."""

from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next


two: Node = Node(2, None)
one: Node = Node(1, two)


def sum(head: Node | None) -> int:
    """Compute sum of values across all nodes in linked list."""
    if head is None:
        return 0
    else:
        rest: int = sum(head.next)
        return head.value + rest


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
