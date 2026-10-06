
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    # The smallest possible sum of 4 positive even numbers is 2+2+2+2=8
    # So, if n is less than 8, it cannot be written as the sum of 4 positive even numbers
    if n < 8:
        return False
    # If n is greater than or equal to 8, it can be written as the sum of 4 positive even numbers if and only if it is even
    # This is because the sum of an even number of even numbers is always even
    return n % 2 == 0
