
def solve(N):
    # Convert the number to binary and remove the '0b' prefix
    binary = bin(N)[2:]
    
    # Calculate the sum of the digits
    sum_of_digits = sum(int(digit) for digit in binary)
    
    # Convert the sum to binary and return it as a string
    return bin(sum_of_digits)[2:]
