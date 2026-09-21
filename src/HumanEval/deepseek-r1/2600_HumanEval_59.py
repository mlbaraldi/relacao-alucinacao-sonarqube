

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    largest = 1
    # Check for the factor 2
    if n % 2 == 0:
        largest = 2
        while n % 2 == 0:
            n = n // 2
    # Check for odd factors starting from 3
    divisor = 3
    while divisor * divisor <= n:
        while n % divisor == 0:
            largest = divisor
            n = n // divisor
        divisor += 2
    # If remaining n is a prime number
    if n > 1:
        largest = n
    return largest
