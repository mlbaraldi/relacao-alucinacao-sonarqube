
def circular_shift(x, shift):
    # Convert the integer to a string
    str_x = str(x)
    
    # If shift is greater than the length of the string, reverse the string
    if shift >= len(str_x):
        return str_x[::-1]
    
    # Otherwise, shift the string
    return str_x[-shift:] + str_x[:-shift]

# Test cases
