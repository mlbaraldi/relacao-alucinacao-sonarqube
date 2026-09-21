import math


def poly(xs: list, x: float):
    # Initial guess
    x = 0.0

    # Iterate until the function value is close enough to zero
    for _ in range(1000):
        # Calculate the function value and its derivative
        f = poly(xs, x)
        df = sum([i * coeff * math.pow(x, i - 1) for i, coeff in enumerate(xs) if i > 0])

        # Update the guess using the Newton-Raphson method
        x -= f / df

        # If the function value is close enough to zero, return the guess
        if abs(f) < 1e-6:
            return x

    # If no root was found, raise an exception
    raise ValueError("No root found")
