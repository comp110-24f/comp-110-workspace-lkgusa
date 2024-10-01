"""Recreating Wordle's game loop"""

__author__ = "730663471"


def input_guess(secret_word_len: int) -> str:
    """Will check if a user guessed word is the same length as the secret word"""
    guess = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    """Will check a word for any instance(s) of a specified character and return T (if it is found) or F (if it isn't found)"""
    index = 0
    count = 0
    while index < len(secret_word):
        check = secret_word[index]
        if check == char_guess:
            count += 1
            index += 1
        else:
            index += 1

    if count >= 1:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)
    """Will check each letter of guess - if guess letter = secret letter, green box added to emoji_string, if guess letter != secret letter but it is somewhere in secret a yellow box will be added, and if the guess letter is nowhere in secret, a white box will be added to the emoji string"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    emoji_string = ""
    while index < len(guess):
        check = guess[index]
        if check == secret[index]:
            emoji_string += GREEN_BOX
        elif contains_char(secret, guess[index]):
            # Originally I had the contains_char function call == True in this line but actually since contains_char will return a bool it doesn't need to be checked equal to true because the value itself is True or False
            # If contains_char is True then the indented line will be read and if it is False then it will skip! the == True was redundant!
            emoji_string += YELLOW_BOX
        else:
            emoji_string += WHITE_BOX
        index += 1
    return emoji_string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len=len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return  # Must add return here so that python won't continue in the while loop after the user guesses secret correctly
            # The return also has to be empty since main does not return any value
        else:
            turn += 1
        if turn > 6:
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
