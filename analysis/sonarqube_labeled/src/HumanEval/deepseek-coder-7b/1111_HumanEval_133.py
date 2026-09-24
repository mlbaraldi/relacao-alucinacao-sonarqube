

def sum_squares(lst):
    return sum(int(x**2) for x in map(lambda x: round(x) if x >= 0 else round(x) - 1, lst))

