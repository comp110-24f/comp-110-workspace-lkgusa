"""Testing functions written for quiz 4 practice."""


# This one I looked at the answer for
def factorial(n: int) -> int:
    """Returns n!"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# # Returns 3 * 2 * 1 = 6
# print(factorial(3))

# # Returns 5 * 4 * 3 * 2 * 1 = 120
# print(factorial(5))


def sum_of_natural_numbers(n: int) -> int:
    """Returns sum of the first n natural numbers."""
    if n == 0:
        return 0
    else:
        return n + sum_of_natural_numbers(n - 1)


# # Returns 5 + 4 + 3 + 2 + 1 = 15
# print(sum_of_natural_numbers(5))

# # Returns 0
# print(sum_of_natural_numbers(0))


def power(val: int, pwr: int) -> int:
    """Returns val raised to pwr using recursion."""
    if pwr == 0:
        return 1
    else:
        return val * power(val, pwr - 1)


def gcd(num1: int, num2: int) -> int:
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
