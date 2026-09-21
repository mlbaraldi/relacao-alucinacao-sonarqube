
def is_multiply_prime(a):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    factors = []
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0 and is_prime(i):
            factors.append(i)
            a /= i
        if a == 1:
            break
    if a > 1 and is_prime(a):
        factors.append(int(a))

    return len(factors) == 3 and all(is_prime(f) for f in factors)

