

def prime_fib(n: int):
    fib_nums = [0, 1]
    prime_fib_nums = []
    while len(prime_fib_nums) < n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
        if is_prime(fib_nums[-1]):
            prime_fib_nums.append(fib_nums[-1])
    return prime_fib_nums[-1]

