

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    # The derivative of a polynomial is a new polynomial where each coefficient is the product of the old coefficient and the exponent, and the exponent is reduced by 1.
    # The derivative of a constant is 0.
    # So we start from the second coefficient and for each coefficient, we multiply it by its corresponding exponent and reduce the exponent by 1.
    # The result is a new list of coefficients.
    # If the original list has only one element (i.e., the polynomial is a constant), the derivative is 0.
    if len(xs) == 1:
        return [0]
    else:
        return [i * xs[idx + 1] for idx, i in enumerate(xs[1:])]

