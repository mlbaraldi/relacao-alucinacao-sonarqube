

def round_half_to_even(n):
    if n - int(n) < 0.5:
        return int(n)
    elif n - int(n) > 0.5:
        return int(n) + 1
    else:
        if int(n) % 2 == 0:
            return int(n)
        else:
            return int(n) + 1
