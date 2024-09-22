"""Practice with conditionals!"""


def less_than_10(num: int) -> bool:
    """Will say if given num < 10"""
    if num < 10:  # Will check if this is true
        return True  # Then block
    else:
        return False


def less_than_10(num: int) -> None:
    """Will say if given num < 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:  # Will check if this is true
        print("Small number")  # Then block
    else:
        print("Big number")
    print("Have a good day sir")


print(less_than_10(num=11))
less_than_10(num=11)
less_than_10(num=11)


def wake_up(alarm: bool) -> str:
    """Return a message based on if alarm is going off"""
    if alarm is True:
        return "Wake up, get up, get out there!"
    else:
        return "Keep sleeping and enjoy the bliss of not being conscious"


print(wake_up(alarm=True))


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is the first character of given word"""
    if word[0] == letter:  # Can also use "is" in place of ==
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
