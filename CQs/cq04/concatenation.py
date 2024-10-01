"""Concatenation functions"""

__author__ = "730663471"

word1: str = "happy"
word2: str = "tuesday"


def concat(str1: str, str2: str) -> str:
    return str1 + str2


if __name__ == "__main__":
    # Calls for concat in this file will only be in this current concatenation file and not carried over to other files where we might call concat
    print(concat(word1, word2))
