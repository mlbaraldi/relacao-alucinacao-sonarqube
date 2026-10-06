

def fibfib(n: int):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fibfib_values = [0, 0, 1] + [0] * (n - 2)
        for i in range(3, n + 1):
            fibfib_values[i] = fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3]
        return fibfib_values[n]

# Test cases
