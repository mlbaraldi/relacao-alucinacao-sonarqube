

def is_palindrome(string: str) -> bool:
    # Find the longest postfix of the string that is a palindrome
    palindrome_postfix = string[::-1]
    for i in range(len(string)):
        if palindrome_postfix[:i] == palindrome_postfix[i:]:
            palindrome_postfix = palindrome_postfix[:i]
            break

    # Append the reverse of the string prefix that comes before the palindromic suffix
    return string + palindrome_postfix[::-1]
