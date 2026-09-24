

def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is also prime.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")

    # Initialize the Fibonacci sequence
    a, b = 0, 1

    # Iterate until we reach the n-th prime Fibonacci number
    for i in range(n):
        a, b = b, a + b
        if is_prime(a):
            return a

    # If we reach this point, we didn't find a prime Fibonacci number
    raise ValueError("No prime Fibonacci number found for n = {}".format(n))

