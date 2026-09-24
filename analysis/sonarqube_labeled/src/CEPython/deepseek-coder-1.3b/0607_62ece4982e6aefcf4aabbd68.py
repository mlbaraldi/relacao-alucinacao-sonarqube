

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    """
    Convert a number to a string, using the given alphabet.

    The output has the most significant digit first.
    """
    if padding is None:
        padding = len(alphabet)

    result = ''
    while number > 0:
        result = alphabet[number % padding] + result
        number //= padding

    return result
