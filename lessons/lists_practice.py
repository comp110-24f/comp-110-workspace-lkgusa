"""Basic list syntax"""

# With constructor
my_numbers: list[float] = list()
# With literal
my_numbers: list[float] = []

# Adds 1.5 to list of my_numbers
# Append only takes one argument
my_numbers.append(1.5)
my_numbers.append(2.3)

# Create a populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription notation/indexing
print(game_points[2])
last_game: int = game_points[2]
print(last_game)

# Modifying by index!!! (lists are mutable)
game_points[1] = 72
print(game_points)

# You can't replace string characters using index (strings are immutable)

# Length of list
print(len(game_points))

# Removing list items
game_points.pop(1)
print(game_points)


# Can make function involving list
def display(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        print(input[index])
        index += 1


display(input=game_points)
game_points.append(94)
print(game_points)
