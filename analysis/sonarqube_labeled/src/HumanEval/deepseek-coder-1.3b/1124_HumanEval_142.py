


def sum_squares(lst):
    return sum(x**3 if i%3==0 else x**2 if i%4==0 else 0 for i, x in enumerate(lst))
