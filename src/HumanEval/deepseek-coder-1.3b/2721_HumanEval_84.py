
def solve(N):
    # Convert the integer to binary and remove the '0b' prefix
    binary = bin(N)[2:]
    
    # Calculate the sum of the digits in the binary number
    sum_of_digits = sum(int(digit) for digit in binary)
    
    # Convert the sum of digits back to a binary string and return it
    return bin(sum_of_digits)[2:]
