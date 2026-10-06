

def is_palindrome(string: str) -> bool:
    """ Find the shortest palindrome that begins with a supplied string. """
    for i in range(len(string) + 1):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    return string
