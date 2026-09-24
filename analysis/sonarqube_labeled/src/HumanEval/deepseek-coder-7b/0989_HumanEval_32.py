import math


def poly(xs: list, x: float):
    """
    xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non-zero coefficient as it guarantees a solution.
    """
    if len(xs) % 2 != 0:
        raise ValueError("The list of coefficients must have an even number of elements.")
    
    # Start with an initial guess, which is the reciprocal of the leading coefficient
    x0 = 1.0 / xs[0]
    
    # Newton-Raphson iteration
    for _ in range(1000):  # Limit the number of iterations to prevent infinite loops
        # Compute the derivative of the polynomial at x0
        derivative = sum([i * coeff * math.pow(x0, i) for i, coeff in enumerate(xs)])
        
        # Check if the derivative is zero to prevent division by zero
        if derivative == 0:
            raise ValueError("The derivative of the polynomial is zero, which means the polynomial has a constant term.")
        
        # Compute the next approximation
        x1 = x0 - poly(xs, x0) / derivative
        
        # Check for convergence
        if abs(x1 - x0) < 1e-10:  #
