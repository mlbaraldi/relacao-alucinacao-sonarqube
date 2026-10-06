from typing import List, Optional


def int_to_string(number: int, alphabet: List[str], padding: Optional[int] = None) -> str:
    base = len(alphabet)
    result = ''
    while number:
        number, i = divmod(number, base)
        result = alphabet[i] + result
    if padding is not None and len(result) < padding:
        result = alphabet[0] * (padding - len(result)) + result
    return result
