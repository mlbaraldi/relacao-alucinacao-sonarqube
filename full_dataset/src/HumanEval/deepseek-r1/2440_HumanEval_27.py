

def flip_case(string: str) -> str:
    flipped = []
    for char in string:
        if char.isupper():
            flipped.append(char.lower())
        elif char.islower():
            flipped.append(char.upper())
        else:
            flipped.append(char)
    return ''.join(flipped)
