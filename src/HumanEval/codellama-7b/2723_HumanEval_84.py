
def solve(N):
    # Convert N to binary
    binary_string = bin(N)[2:]
    
    # Calculate the sum of the digits
    sum_of_digits = 0
    for digit in binary_string:
        sum_of_digits += int(digit)
    
    # Return the sum as a string
    return str(sum_of_digits)
