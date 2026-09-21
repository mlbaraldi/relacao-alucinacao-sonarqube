
def reverse_delete(s,c):
    # Create a new string by removing all characters in s that are in c
    new_string = ''.join([char for char in s if char not in c])

    # Check if the new string is a palindrome
    is_palindrome = new_string == new_string[::-1]

    return (new_string, is_palindrome)
