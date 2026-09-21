
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    # Initialize the tuple to store the number of even and odd palindromes
    even_palindromes = 0
    odd_palindromes = 0

    # Iterate through the range of integers from 1 to n
    for i in range(1, n+1):
        # Check if the integer is a palindrome
        if is_palindrome(i):
            # If the integer is even, increment the number of even palindromes
            if i % 2 == 0:
                even_palindromes += 1
            # Otherwise, increment the number of odd palindromes
            else:
                odd_palindromes += 1

    # Return the tuple of even and odd palindromes
    return (even_palindromes, odd_palindromes)

# Helper function to check if an integer is a palindrome
