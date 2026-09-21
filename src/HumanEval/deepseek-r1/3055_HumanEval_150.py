
def x_or_y(n, x, y):
    if n <= 1:
        return y
    if n == 2:
        return x
    if n % 2 == 0:
        return y
    max_divisor = int(n ** 0.5) + 1
    for i in range(3, max_divisor, 2):
        if n % i == 0:
            return y
    return x
