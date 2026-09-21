
def is_multiply_prime(a):
    def prime_factors(n):
        factors = []
        # Handle division by 2
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
        # Check odd divisors up to sqrt(n)
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n = n // i
            i += 2
        # If remaining n is a prime
        if n > 2:
            factors.append(n)
        return factors
    
    if a < 2:
        return False
    factors = prime_factors(a)
    return len(factors) == 3
