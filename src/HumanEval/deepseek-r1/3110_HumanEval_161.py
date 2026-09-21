
def solve(s):
    has_letters = any(c.isalpha() for c in s)
    transformed = []
    for char in s:
        if char.isalpha():
            transformed.append(char.swapcase())
        else:
            transformed.append(char)
    transformed_str = ''.join(transformed)
    return transformed_str[::-1] if not has_letters else transformed_str
