
def solve(s):
    result = ''
    for char in s:
        if char.isalpha():
            if char.islower():
                result += char.upper()
            else:
                result += char.lower()
        else:
            result += char[::-1]
    return result[::-1] if not any(char.isalpha() for char in s) else result
