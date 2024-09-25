"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730663471"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    chosen_word: str = input("Enter a 5-character word: ")
    if len(chosen_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        return chosen_word

    else:
        return chosen_word


def input_letter() -> str:
    chosen_character: str = input("Enter a single character: ")
    if (
        len(chosen_character) != 1
    ):  # If the length of chosen_character is not equal to 1, then...
        print("Error: Character must be a single character.")
        exit()
        return chosen_character
    else:  # If this line is read then the length of chosen_character must be 1 and chosen_word can then be passed to contains_char
        return chosen_character


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + str(letter) + " in " + str(word))
    index: int = 0
    count: int = 0
    while index < len(word) - 1:
        if word[index] == letter:
            count += 1
            print(str(letter) + " found at index " + str(index))
            index += 1
        else:
            index += 1

    if count == 0:  # If no letter was found in word, print no instances
        print("No instances of " + str(letter) + " found in " + str(word))
    elif count == 1:  # If only 1 letter was found in word, print count INSTANCE
        print(str(count) + " instance of " + str(letter) + " found in " + str(word))
    else:  # If more than 1 letter was found in word, print count INSTANCES
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))


if __name__ == "__main__":
    main()
