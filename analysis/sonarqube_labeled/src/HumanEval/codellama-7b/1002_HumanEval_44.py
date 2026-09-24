

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    """
    # Convert the input number to a string in the given base
    num_str = str(x)
    # Create a list to store the digits of the converted number
    converted_digits = []
    # Loop through each digit of the input number
    for digit in num_str:
        # Convert the digit to the target base
        converted_digit = str(int(digit, base))
        # Add the converted digit to the list
        converted_digits.append(converted_digit)
    # Join the list of converted digits into a single string
    converted_num_str = "".join(converted_digits)
    # Return the string representation of the converted number
    return converted_num_str
