import numpy as np


def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.

    Coordinates outside the histogram edges are ignored.
    """
    if all(c >= 0 and c < s for c, s in zip(coord, self.hist.shape)):
        self.hist[tuple(coord)] += weight
