
def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the primes less than n."""
    if n <= 1:
        return []
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for current in range(2, int((n - 1) ** 0.5) + 1):
        if sieve[current]:
            for multiple in range(current * current, n, current):
                sieve[multiple] = False
    primes = [i for i in range(2, n) if sieve[i]]
    return primes
