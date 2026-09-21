
def any_int(x, y, z):
    # Check if all inputs are integers
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    # Check if any of the inputs is equal to the sum of the other two
    return x == (y + z) or y == (x + z) or z == (x + y)
