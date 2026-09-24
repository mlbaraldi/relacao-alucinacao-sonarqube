
def hex_key(num):
    # Convert the input string to a list of hexadecimal digits
    hex_digits = [c for c in num if c in "0123456789ABCDEF"]

    # Initialize a counter for the number of prime digits
    prime_count = 0

    # Iterate over the hexadecimal digits
    for digit in hex_digits:
        # Convert the current digit to an integer
        digit_int = int(digit, 16)

        # Check if the current digit is prime
        if is_prime(digit_int):
            # Increment the counter if the current digit is prime
            prime_count += 1

    # Return the number of prime digits
    return prime_count

# Check if a number is prime
