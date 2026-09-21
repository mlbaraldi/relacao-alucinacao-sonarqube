
def hex_key(num):
    # Define the prime hexadecimal digits
    prime_hex_digits = set('2357BD')
    
    # Count the number of prime hexadecimal digits in the input string
    return sum(1 for digit in num if digit in prime_hex_digits)
