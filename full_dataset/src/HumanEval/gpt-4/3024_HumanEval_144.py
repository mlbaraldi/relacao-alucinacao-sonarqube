
def simplify(x, n):
    # Split the fractions into numerator and denominator
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    # Multiply the fractions
    result = (x_num * n_num) / (x_den * n_den)

    # Check if the result is a whole number
    return result.is_integer()
