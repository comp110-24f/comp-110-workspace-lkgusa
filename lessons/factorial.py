"""Writing a factorial function using recursion in class 11/18."""


def factorial(n: int) -> int:
    """Calculates factorial of int n"""
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)


print(factorial(3))
