import math


def poly(xs: list, x: float):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    # Check if the list xs has even number of coefficients
    if len(xs) % 2 != 0:
        raise ValueError("The list xs must have an even number of coefficients")

    # Find the largest non-zero coefficient
    non_zero_coeff = max(filter(lambda coeff: coeff != 0, xs), default=0)

    # Find the roots of the polynomial
    roots = [(-b + math.sqrt(b**2 - 4*a*c)) / (2*a) for a, b, c in [(1, non_zero_coeff, xs[i+1]) for i in range(len(xs)//2)]]

    # Return the roots that are close enough to zero
