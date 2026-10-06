

def round_half_to_even(n):
    if n % 2 == 0:
        return int(n)
    else:
        return int(n) + 1 if n > 0 else int(n) - 1
