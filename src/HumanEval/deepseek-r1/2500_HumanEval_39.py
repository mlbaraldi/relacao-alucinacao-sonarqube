

def prime_fib(n: int):
    """
    prime_fib returns the n-th number that is a Fibonacci number and also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True
    
    primes = []
    fib_prev, fib_curr = 0, 1
    while len(primes) < n:
        next_fib = fib_prev + fib_curr
        if is_prime(next_fib):
            primes.append(next_fib)
        fib_prev, fib_curr = fib_curr, next_fib
    return primes[-1]
