"""My first  challenge question in COMP110!"""

__author__ = "730663471"


def mimic(message: str) -> str:
    """This function will repeat a message entered by the user back to them, like an annoying younger sibling might!"""
    return message


def main() -> None:
    """This function will print the result of calling the mimic function defined earler"""
    print(mimic(message=input("What is your message?")))
    return None


if __name__ == "__main__":
    main()
