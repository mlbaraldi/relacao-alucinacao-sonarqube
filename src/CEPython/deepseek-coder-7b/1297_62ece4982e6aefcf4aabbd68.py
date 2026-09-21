from typing import List, Optional


def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    """
    Convert a number to a string, using the given alphabet.

    The output has the most significant digit first.
    """
    result = ""
    while number > 0:
        result = alphabet[number % len(alphabet)] + result
        number //= len(alphabet)

    if padding is not None:
        result = result.zfill(padding)

    return result
