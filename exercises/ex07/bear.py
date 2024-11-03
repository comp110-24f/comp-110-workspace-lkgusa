"""File to define Bear class."""

__author__ = "730663471"


class Bear:
    """Bear class defines age and hunger mechanics of each bear in list."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializes age and hunger of each bear."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Ages each bear by 1 and deducts 1 from bear hunger_score per day."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """hunger_score is updated to the num_fish the bear ate."""
        self.hunger_score += num_fish
        return None
