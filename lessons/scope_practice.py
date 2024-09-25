"""Some scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed"""
    copy: str = ""  # Empty string with values that can be copied over
    index: int = 0
    while index < len(msg):
        if not (
            msg[index] == char
        ):  # Index here is a subscription notation, with brackets around it
            # Used to access one character from a number or word at a time
            copy += msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    # If running this file directly, implement these lines of code
    word: str = "yoyo"  # This is a global variable
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))

# Keyword arguments are msg = "", char = ""
# Positional arguments are just saying word, "y"
# As long as arguments are in the right order, you can put arguments directly
# into remove_chars()
