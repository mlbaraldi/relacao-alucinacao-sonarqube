
def is_simple_power(x, n):
    if x < 1 or n < 1:
        return False
    power = round(x ** (1.0 / n))
    return n ** power == x
