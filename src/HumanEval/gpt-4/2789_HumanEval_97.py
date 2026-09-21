
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    """
    # Get the unit digit of a and b by taking the modulus of 10
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10

    # Return the product of the unit digits
    return unit_digit_a * unit_digit_b
