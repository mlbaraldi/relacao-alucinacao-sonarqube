import math


def poly(xs: list, x: float):
    import math
    # Compute the derivative coefficients
    der_coeff = [i * coeff for i, coeff in enumerate(xs) if i > 0]
    
    # Newton-Raphson method
    x_nr = 0.0
    epsilon = 1e-7
    max_iterations = 1000
    for _ in range(max_iterations):
        fx = poly(xs, x_nr)
        if abs(fx) < epsilon:
            return x_nr
        if not der_coeff:  # Handle case where derivative is zero polynomial
            break
        dfx = poly(der_coeff, x_nr)
        if dfx == 0:
            break  # Newton-Raphson can't proceed, switch to bisection
        x_new = x_nr - fx / dfx
        if abs(x_new - x_nr) < epsilon:
            return x_new
        x_nr = x_new
    
    # Fallback to bisection method
    a = -1.0
    b = 1.0
    fa = poly(xs, a)
    fb = poly(xs, b)
    
    # Expand interval until signs are opposite
    while fa * fb >= 0:
        a *= 2
        b *= 2
        fa = poly(xs, a)
        fb = poly(xs, b)
    
    # Bisection loop
    while b - a > epsilon:
        mid = (a + b) / 2
        f_mid = poly(xs, mid)
        if f_mid == 0:
            return mid
        if fa * f_mid < 0:
            b = mid
            fb = f_mid
        else:
            a = mid
            fa = f_mid
    
    return (a + b) / 2
