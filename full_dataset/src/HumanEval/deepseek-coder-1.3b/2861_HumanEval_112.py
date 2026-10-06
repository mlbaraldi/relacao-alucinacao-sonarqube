
def reverse_delete(s,c):
    # Remove characters in s that are in c
    s = ''.join([i for i in s if i not in c])
    # Check if s is a palindrome
    is_palindrome = s == s[::-1]
    # Return the result string and the palindrome check
    return (s, is_palindrome)
