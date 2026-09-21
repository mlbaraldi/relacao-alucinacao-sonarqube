def round_half_to_even(n):
    import math
    if n == int(n):
        return int(n)
    fractional, integer_part = math.modf(n)
    integer = int(integer_part)
    if abs(fractional) == 0.5:
        if fractional > 0:
            candidates = [integer, integer + 1]
        else:
            candidates = [integer, integer - 1]
        # Find the even candidate
        for c in candidates:
            if c % 2 == 0:
                return c
    else:
        if fractional >= 0.5 or fractional <= -0.5:
            if fractional > 0:
                return integer + 1
            else:
                return integer - 1
        else:
            return integer
