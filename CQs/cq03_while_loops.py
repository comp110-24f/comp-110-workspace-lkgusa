"""Practice with while lopps"""

__author__ = "730663471"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = (
        0  # Sets count equal to 0 (what will be increased each time search_char is found in phrase)
    )
    index: int = (
        0  # Sets index equal to 0 (it will be increased to look through each letter of phrase)
    )
    while index < len(phrase) - 1:  # Subtracting one since python begins counting at 0
        # The length of a given phrase counts like humans so len("cat") would be 3 but "cat"[3] would give an error since "cat"[2] returns the last letter in cat instead
        # Need to subtract one from the length output of the phrase so python won't try to count outside of the phrase string
        if (
            phrase[index] == search_char
        ):  # If a character in phrase is equal to the search_char
            count = count + 1  # Add one to the count value
        index = (
            index + 1
        )  # REGARDLESS of if a search_char instance was found in phrase, add one to index so it can move on to the next letter in phrase (this is why it is outside of the if indent)
        # This while loop will repeat until the index is no longer less than the phrase length to find all possible instances of search_char
    return count  # Record the number of search_char instances found in phrase
