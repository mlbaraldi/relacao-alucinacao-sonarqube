
def choose_num(x, y):
    import math
    """Return the largest even integer in [x, y] inclusive, or -1 if none exists."""
    if x > y:
        return -1
    floor_y = math.floor(y)
    if floor_y % 2 != 0:
        max_even = floor_y - 1
    else:
        max_even = floor_y
    max_even = int(max_even)
    return max_even if max_even >= x else -1
