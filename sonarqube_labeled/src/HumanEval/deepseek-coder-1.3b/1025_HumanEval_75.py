
def is_multiply_prime(a):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    factors = []
    for i in range(2, a + 1):
        if a % i == 0 and is_prime(i):
            factors.append(i)
            a //= i
            if len(factors) > 3:
                return False
    return len(factors) == 3 and is_prime(a)
