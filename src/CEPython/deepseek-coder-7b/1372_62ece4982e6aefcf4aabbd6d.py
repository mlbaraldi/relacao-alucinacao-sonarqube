from typing import List


def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    Convert a string to a number, using the given alphabet.

    The input is assumed to have the most significant digit first.
    """
    alphabet_dict = {char: i for i, char in enumerate(alphabet)}
    num = 0
    for char in string:
        num = num * len(alphabet) + alphabet_dict[char]
    return num
