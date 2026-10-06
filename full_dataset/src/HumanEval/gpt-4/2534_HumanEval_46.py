

def fib4(n: int):
    if n < 0:
        raise ValueError("Negative arguments are not supported.")
    elif n <= 3:
        return [0, 0, 2, 0][n]
    else:
        fib = [0, 0, 2, 0] + [0] * (n - 3)
        for i in range(4, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2] + fib[i - 3] + fib[i - 4]
        return fib[n]
