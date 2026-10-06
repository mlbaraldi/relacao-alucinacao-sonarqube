
def closest_integer(value):
    import math
    x = float(value)
    integer_part = math.floor(x)
    fractional_part = x - integer_part
    if fractional_part == 0.5:
        if x >= 0:
            return int(x + 0.5)
        else:
            return int(x - 0.5)
    else:
        if fractional_part >= 0.5:
            return integer_part + 1
        else:
            return integer_part
