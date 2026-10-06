
def solve(s):
    result = ""
    for i in range(len(s)):
        if s[i].isalpha():
            result += s[i].swapcase()
        else:
            result += s[i]
    return result
