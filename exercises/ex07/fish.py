"""File to define Fish class."""

__author__ = "730663471"


class Fish:
    """Fish class defines age mechanics of each fish in list."""

    age: int

    def __init__(self):
        """Initializes the age of each fish."""
        self.age = 0
        return None

    def one_day(self):
        """Ages each fish by 1 per day."""
        self.age += 1
        return None
