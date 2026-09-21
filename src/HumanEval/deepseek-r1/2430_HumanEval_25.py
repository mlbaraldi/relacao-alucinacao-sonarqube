from typing import List


def factorize(n: int) -> List[int]:
    from typing import List
    factors = []
    # Handle the factor of 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # Now n must be odd, check odd divisors starting from 3
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n = n // d
        d += 2
    # If remaining n is a prime
    if n > 1:
        factors.append(n)
    return factors
