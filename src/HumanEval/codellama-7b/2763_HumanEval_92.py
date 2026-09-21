
def any_int(x, y, z):
    if not all(isinstance(n, int) for n in (x, y, z)):
        return False
    if x == y + z:
        return True
    if y == x + z:
        return True
    if z == x + y:
        return True
    return False
