

def string_to_int(string: str, alphabet: List[str]) -> int:
    result = 0
    for i, char in enumerate(string):
        result += alphabet.index(char) * (len(alphabet) ** (len(string) - i - 1))
    return result
