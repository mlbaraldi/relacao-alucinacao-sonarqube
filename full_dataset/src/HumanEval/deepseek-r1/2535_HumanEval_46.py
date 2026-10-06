

def fib4(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0
    else:
        a, b, c, d = 0, 0, 2, 0  # fib4(0), fib4(1), fib4(2), fib4(3)
        for k in range(4, n + 1):
            current = a + b + c + d
            a, b, c, d = b, c, d, current
        return d
