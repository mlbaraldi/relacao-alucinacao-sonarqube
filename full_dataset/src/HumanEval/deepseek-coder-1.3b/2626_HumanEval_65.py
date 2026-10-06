
def circular_shift(x, shift):
    # Convert the integer to a string
    x_str = str(x)
    
    # Calculate the number of digits in the integer
    num_digits = len(x_str)
    
    # Calculate the new position of the shift
    new_pos = (num_digits + shift) % num_digits
    
    # Return the circular shifted string
    return x_str[-new_pos:] + x_str[:-new_pos]

# Test the function
