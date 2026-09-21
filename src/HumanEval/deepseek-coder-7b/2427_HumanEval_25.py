from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    # Divide n by 2 until it's no longer divisible
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    # n must be odd at this point, so we can skip one element (we've checked 2)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    # This condition is to handle the case when n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

# Test cases
