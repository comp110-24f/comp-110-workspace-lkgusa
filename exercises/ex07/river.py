"""File to define River class."""

__author__ = "730663471"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """River class defines bear and fish interactions and time passing mechanics."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks ages of fish and bears; if over specified age, remove from list."""
        surviving_bears: list[Bear] = []  # Create empty list for bears alive
        surviving_fish: list[Fish] = []  # Create empty list for fish alive
        for bear in self.bears:  # For every bear,
            if bear.age <= 5:
                surviving_bears.append(bear)
                # If bear is less than 5, add to surviving_bears
        self.bears = surviving_bears
        # Only keeps surviving_bears in bear list
        for fish in self.fish:  # For every fish,
            if fish.age <= 3:
                surviving_fish.append(fish)
                # If fish is less than 3, add to surviving_fish
        self.fish = surviving_fish
        # Only keeps surviving_fish in fish list
        return None

    def bears_eating(self):
        """If there are enough fish, will make each bear eat 3 fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Checks each bear's hunger, if it hasn't eaten, remove it from bear list."""
        sated_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score < 0:
                sated_bears.append(bear)
        self.bears = sated_bears

        return None

    def repopulate_fish(self):
        """For every two fish in fish list, add a new fish."""
        # Calculates the number of new fish to add
        new_fish_to_add = (len(self.fish) // 2) * 4
        # Adds a new fish to fish list new_fish_to_add times
        for fish in range(new_fish_to_add):
            self.fish.append(Fish())
            # Adds a new fish to fish list
        return None

    def repopulate_bears(self):
        """For every two bears in bears list, add a new bear."""
        # Calculates the number of new bears to add
        new_bears_to_add = len(self.bears) // 2
        # Adds a new bear to bears list new_bears_to_add times
        for bear in range(new_bears_to_add):
            self.bears.append(Bear())
            # Adds a new bear to bears list
        return None

    def view_river(self):
        """Prints river stats."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates one week of life in the river."""
        for i in range(7):
            self.one_river_day()
            # Calls one_river_day() 7 times

    def remove_fish(self, amount: int):
        """Remove amount fish from the front of fish list."""
        # What if amount > fish?

        for fish in range(amount):
            self.fish.pop(0)
            # For amount fish in fish, remove the first fish in list
        return None
