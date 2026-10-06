import math


def poly(xs: list, x: float):
    """
    Finds the zero point of a polynomial with coefficients xs.
    The function assumes that the polynomial has an even number of coefficients
    and that the largest non-zero coefficient is guaranteed to be positive.
    """
    # Check if the polynomial has an even number of coefficients
    if len(xs) % 2 == 1:
        raise ValueError("Polynomial must have an even number of coefficients")

    # Find the largest non-zero coefficient
    largest_coeff = max(xs)

    # Check if the largest coefficient is positive
    if largest_coeff <= 0:
        raise ValueError("Largest coefficient must be positive")

    # Find the zero point by iterating over the range of x values
    x_values = np.linspace(0, 1, 100)
    for x in x_values:
        if poly(xs, x) == 0:
            return x

    # If no zero point is found, return None
    return None
