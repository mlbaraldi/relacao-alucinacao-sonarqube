import math


def gaussian(x):
    """
    Gaussian centered around mu with a standard deviation of sigma.
    """
    return (1 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(-((x - mu) ** 2 / (2 * sigma ** 2)))
