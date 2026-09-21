

def prime_fib(n: int):
    count = 0
    i = 1
    while count < n:
        fib = fibonacci(i)
        if is_prime(fib):
            count += 1
        i += 1
    return fibonacci(i - 1)
