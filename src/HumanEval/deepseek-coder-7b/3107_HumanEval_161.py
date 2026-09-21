
def solve(s):
    if not any(c.isalpha() for c in s):
        return s[::-1]
    else:
        return ''.join(c.upper() if c.islower() else c.lower() for c in s)

