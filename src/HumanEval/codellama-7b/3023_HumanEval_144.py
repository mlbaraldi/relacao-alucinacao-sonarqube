
def simplify(x, n):
    x_numerator, x_denominator = x.split('/')
    n_numerator, n_denominator = n.split('/')
    if x_denominator == n_denominator:
        return True
    else:
        return False
