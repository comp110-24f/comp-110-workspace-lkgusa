"""Practice with functions"""

from random import randint

print(randint(1, 10))


# Defining a function
def sum(num1: int, num2: int) -> int:  # This is the parameter list (the signature)
    """Returns sum of num1 + num2"""
    return num1 + num2


# Calling a function
randint(1, 10)
print(
    sum(num1=1, num2=10)
)  # 1 and 10 are the arguments, this is an argument list since there are specific arguments being defined
sum(
    num1=randint(1, 10), num2=randint(2, 20)
)  # Summing random integers, assigning parameter
