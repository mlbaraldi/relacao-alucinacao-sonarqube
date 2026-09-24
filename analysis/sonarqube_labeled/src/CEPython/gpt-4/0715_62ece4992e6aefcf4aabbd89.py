import math


def gaussian(x):
    mu = 0.2
    sigma = 0.1
    return (1.0 / (math.sqrt(2 * math.pi * sigma**2))) * math.exp(-((x - mu)**2) / (2 * sigma**2))
