"""Dictionary utility functions"""

__author__ = "730663471"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary with the keys being the input dictionary's values and the values being the input dictionary's keys"""
    inverted: dict[str, str] = {}  # Establish secondary dictionary, stores inverted values
    # Can't iterate over a list while modifying it
    for item in input:
        key: str = item  # Key variable stores key values
        val: str = input[item]  # Val variable stores values associated with keys
        if val in inverted:  # Checks if an indentical value was already added to inverted dict
            # If it is, it means it can't be added since you can't have two identical keys
            raise KeyError("Impossible to invert multiple keys with same vals")
        inverted[val] = key  # Converts value of inverted to its key value, this does the actual inversion
    return inverted  # Returns new dict with inverted input dict


def favorite_color(input: dict[str, str]) -> str:
    """Returns a string which is the name of the color the most names said is their favorite"""
    empty: str = "" # Establish empty string for when input is an empty dict
    count: dict[str, int] = {}  # Create new dictionary to store input values and the number of times they appear in input dict

    if len(input) == 0: # When input is empty
        return empty # Return an empty string
    
    for key in input:  # Iterate over each key in input dict,
        val: str = input[key]  # Val variable is set equal to dict value at this key
        if val in count:  # Checks if value (color in this case) has been added to count dict before
            count[val] += 1  # If it has, add 1 to the count value associated with this key value (color) Ex: {"blue": 1} -> {"blue": 2}
        else:
            count[val] = 1  # If this color value isn't in the dictionary yet, add the color and count it once, Ex: {"yellow: 1"} -> {"yellow": 1, "red": 1}
    # Now that count has been established with the number of times favorite colors are tallied
    popular_color: str = ""  # Make an empty string that will document the color most people said is favorite
    tally: int = 0  # Set counting variable equal to 0
    for item in count:  # Iterate over every item in count dict
        if count[item] > tally:  # If the value of count at current index is greater than the tally value
            popular_color = item  # Set the popular color value equal to the color with more counts than current tally
            tally = count[item]  # Set the tally equal to the new greatest amount
    return popular_color  # Return the final string value of the most popular color


def count(input: list[str]) -> dict[str, int]:
    """Returns a dictionary with each key being a value in the given list and each key's value being the number of times that value is seen in the given list"""
    stored: dict[str, int] = {}  # Empty dict to store list items
    for value in input:  # For every value in the input list
        if value in stored:  # If this value is already in the dictionary, 
            stored[value] += 1  # update the count of that value in the dictionary by adding 1
        else:  # If this value is not in the dictionary yet as a key,
            stored[value] = 1  # Add it to the dictionary with a count value of 1
    return stored


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Returns a dictionary of keys that are alphabet letters and list values that are words in given string list that begin with that key's letter"""
    sorted: dict[str, list[str]] = {}  # Empty dictionary containing string keys with associated string lists
    for word in input:  # Iterate over each string in input,
        first_letter: str = word[0].lower()  # Establish first letter as lowercase letter at index 0 of input strings
        if first_letter in sorted:  # If the first_letter is already in sorted as a key,
            sorted[first_letter].append(word)  # Add the word with this first_letter to the end of the established string list
        else:  # If this first_letter is not a key in sorted
            sorted[first_letter] = []  # Create an empty string list to add the word to for this new first_letter
            sorted[first_letter].append(word)  # Add the word with this first_letter to the new string list
    return sorted  # Return the created dictionary


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Mutates given dictionary and returns its modified dictionary with new attendance records"""
    if day not in attendance_log:  # If given day isn't a key in the dictionary,
        attendance_log[day] = [student]  # Add it and also create its corresponding list which will contain the student's name that was there that day
    if student not in attendance_log[day]:  # If given student's name is not a value in the attendance log at given day,
        attendance_log[day].append(student)  # Add the student's name to that day's list














