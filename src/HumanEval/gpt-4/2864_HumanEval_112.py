
def reverse_delete(s,c):
    # Delete all the characters in s that are equal to any character in c
    result = ''.join([i for i in s if i not in c])
    
    # Check if the result string is palindrome
    is_palindrome = result == result[::-1]
    
    return (result, is_palindrome)
