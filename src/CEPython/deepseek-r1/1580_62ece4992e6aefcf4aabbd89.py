def gaussian(x):
    import math
    """
    Gaussian centered around 0.2 with a sigma of 0.1.
    """
    mu = 0.2
    sigma = 0.1
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    return coefficient * math.exp(exponent)
