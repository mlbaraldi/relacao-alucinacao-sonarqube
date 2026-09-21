

def fib4(n: int):
    if n <= 1:
        return 0
    else:
        a, b, c = 0, 0, 0
        for i in range(n-1):
            a, b, c = b, c, a + b + c
        return a + b + c
