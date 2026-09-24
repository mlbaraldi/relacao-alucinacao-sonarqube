
def solve(N):
    # Convert the number to binary
    binary = bin(N)[2:]
    # Calculate the sum of the digits
    sum_digits = sum(int(digit) for digit in binary)
    # Convert the sum to binary
    binary_sum = bin(sum_digits)[2:]
    return binary_sum
