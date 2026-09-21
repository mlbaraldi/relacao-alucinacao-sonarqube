
def hex_key(num):
    # Define the prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    
    # Initialize the count
    count = 0
    
    # Iterate over the hexadecimal digits
    for digit in num:
        # If the digit is a prime number, increment the count
        if digit in primes:
            count += 1
    
    # Return the count
    return count
