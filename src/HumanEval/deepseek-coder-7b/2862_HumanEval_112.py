
def reverse_delete(s,c):
    # Remove all characters in s that are in c
    s = ''.join([char for char in s if char not in c])
    
    # Check if the result string is palindrome
    is_palindrome = s == s[::-1]
    
    return (s, is_palindrome)
