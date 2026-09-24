

def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    if number < 0:
        raise ValueError("Number must be non-negative")
    if len(alphabet) < 2:
        raise ValueError("Alphabet must have at least 2 characters")
    if padding is not None and padding < 0:
        raise ValueError("Padding must be non-negative")

    result = ""
    while number > 0:
        result = alphabet[number % len(alphabet)] + result
        number //= len(alphabet)

    if padding is not None:
        result = result.rjust(padding, alphabet[0])

    return result
