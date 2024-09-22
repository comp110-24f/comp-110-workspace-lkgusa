"""Chardle, a more rudimentary version of Wordle that can be played in the terminal!"""

__author__ = "730663471"


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())
    exit()  # I added this exit function here because otherwise the main function kept repeating;
    # After the count of letter in word were printed, I was prompted to Enter a 5-character word again and the cycle would repeat and you couldn't escape it was kind of overwhelming and scary


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


def contains_char(word, letter) -> None:
    index: int = 0  # Python should begin searching word at the first letter
    count: int = 0  # The count of letter in word should begin at 0
    print("Searching for " + str(letter) + " in " + str(word))
    # Since while loops are not being used here, I think a series of if statements is a way for each index of word to be checked
    # At first I tried to use elif within one if statement but you can't include the index += 1 line outside of the if indent and then try to add an elif line after the index += 1 line, there is an error indication
    if word[index] == letter:
        print(str(letter) + " found at index " + str(index))
        count += 1  # Since there was an instance of letter found, add 1 to count
    index += 1
    if word[index] == letter:
        print(str(letter) + " found at index " + str(index))
        count += 1
    index += 1
    if word[index] == letter:
        print(str(letter) + " found at index " + str(index))
        count += 1
    index += 1
    if word[index] == letter:
        print(str(letter) + " found at index " + str(index))
        count += 1
    index += 1
    if word[index] == letter:
        print(str(letter) + " found at index " + str(index))
        count += 1
    index += 1
    if count == 0:  # If no letter was found in word, print no instances
        print("No instances of " + str(letter) + " found in " + str(word))
    elif count == 1:  # If only 1 letter was found in word, print count INSTANCE
        print(str(count) + " instance of " + str(letter) + " found in " + str(word))
    else:  # If more than 1 letter was found in word, print count INSTANCES
        print(str(count) + " instances of " + str(letter) + " found in " + str(word))


main()  # Calling the main function

if __name__ == "__main__":
    main()
