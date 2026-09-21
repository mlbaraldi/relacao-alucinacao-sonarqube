

def fibfib(n: int):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        x, y, z = 0, 0, 1
        for i in range(3, n + 1):
            next_val = x + y + z
            x = y
            y = z
            z = next_val
        return z
