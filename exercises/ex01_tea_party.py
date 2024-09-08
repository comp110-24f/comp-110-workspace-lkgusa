"""Tea party!"""

__author__ = "730663471"


def main_planner(guests: int) -> None:
    """This main function will combine the three other functions together harmoniously to determine the cost and materials needed to host a tea party given a number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    # At first the I was very confused about the cost function call,
    # initially I tried to just type str(cost(guests, guests)) similar to the previous three lines but that was incorrect because
    # that only inputs the number of guests multiplied by the cost of each tea bag and treat, not accounting so guests can have two tea bags and 1.5 treats per cup of tea
    # I realized that what should really be typed here is tea_bags and treats of guests input into the cost function call - that finally yielded the correct cost!
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """This function will compute the number of total number of tea bags needed so that guests will be able to have two tea bags each"""
    return people * 2


def treats(people: int) -> int:
    """This function will compute the total number of treats needed so that each guest can have approximately 1.5 treats per cup of tea they drink"""
    return tea_bags(int(people * 1.5))


def cost(tea_count: int, treat_count: int) -> float:
    """This function will compute the total cost of tea bags and treats needed to make this tea party a success"""
    # The line below presented some problems for me initially because I was trying to use the people parameter instead of tea_count and treat_count since a value that included people was returned in the previous two function definitions
    # But the correct result was actually much more straightforward than I was first making it! All you have to do it set tea_count and treat_count to integers and multiply those respective values by their cost per unit and add them together as a float!
    return float(int(tea_count) * 0.50 + int(treat_count) * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
