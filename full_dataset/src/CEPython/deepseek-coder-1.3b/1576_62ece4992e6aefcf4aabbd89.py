import math


def gaussian(x):
    """
    Gaussian centered around 0.2 with a sigma of 0.1.
    """
    sigma = 0.1
    mean = 0.2
    exponent = -((x-mean)**2 / (2 * sigma**2))
    gaussian_val = (1 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(exponent)
    return gaussian_val
