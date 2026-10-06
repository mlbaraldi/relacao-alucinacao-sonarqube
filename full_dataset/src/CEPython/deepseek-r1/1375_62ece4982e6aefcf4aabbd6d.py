def string_to_int(string: str, alphabet: List[str]) -> int:
    from typing import List
    base = len(alphabet)
    result = 0
    length = len(string)
    for i in range(length):
        c = string[i]
        digit = alphabet.index(c)
        exponent = length - 1 - i
        result += digit * (base ** exponent)
    return result
