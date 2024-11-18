"""Practice with linked lists in class 11/13."""

from __future__ import annotations


class Node:
    """Node class will create new Node objects."""

    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        """Initializes a new Node object."""
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
        return f"{self.value} -> {str(rest)}"


def value_at(head: Node | None, index: int) -> int:
    """Returns value of Node stored at given index."""
    # Base case 1
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    # Base case 2
    elif index == 0:
        return head.value
    else:
        # Recursive case
        # Calls itself, moves to next node and decreases the index
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Finds the maximum value in the linked list."""
    # Base case 1, linked list is empty
    if head is None:
        raise ValueError("Cannot call max with None")
    # Base case 2, head.value is the last value
    elif head.next is None:
        return head.value
    # Recursive case
    else:
        # Finds the max value of the rest of the list using recursion
        max_of_rest = max(head.next)
        # If the current value of list is greater than the value of the next one
        if head.value > max_of_rest:
            # Make head.value the max
            return head.value
        else:
            # If not, then make max_of_rest (the next value) the max instead
            return max_of_rest


def linkify(items: list[int]) -> Node | None:
    """Returns a linked list of nodes based on an integer list."""
    # Base case, list is empty
    if len(items) == 0:
        return None
    # Define first list value
    first = items[0]
    # Define the rest of the list values
    rest = linkify(items[1:])
    # Returns a linked list of nodes of all of the list values
    return Node(first, rest)


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns linked list of Nodes, each value in original list scaled by factor."""
    # Base case, list is empty
    if head is None:
        return None
    else:
        # Recursive case, scale current value
        scaled_val = head.value * factor
        # Then scale the rest of the list values
        scaled_rest = scale(head.next, factor)
        # Return the linked list of Nodes created
        return Node(scaled_val, scaled_rest)
