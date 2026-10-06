
def is_simple_power(x, n):
    if x == 1:
        return True
    if n == 1:
        return x == 1
    power = 1
    while n ** power <= x:
        if n ** power == x:
            return True
        power += 1
    return False
