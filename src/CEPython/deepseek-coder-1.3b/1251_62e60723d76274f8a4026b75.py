

def round_half_to_even(n):
    """
    Round half to even.

    :param n: The number to round.
    :return: The rounded number.
    """
    return round(n + 0.5 * (1 if n >= 0 else -1))
