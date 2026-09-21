
def simplify(x, n):
    x_fraction = Fraction(int(x.split('/')[0]), int(x.split('/')[1]))
    n_fraction = Fraction(int(n.split('/')[0]), int(n.split('/')[1]))
    result = x_fraction * n_fraction
    return result.denominator == 1

