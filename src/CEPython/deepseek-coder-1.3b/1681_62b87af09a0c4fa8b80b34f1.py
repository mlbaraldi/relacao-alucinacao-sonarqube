

def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.

    Coordinates outside the histogram edges are ignored.
    """
    # Check if the coordinates are within the histogram's edges
    if not self.is_in_bounds(coord):
        return

    # Get the histogram's data
    histogram = self.get_histogram()

    # Fill the histogram at the given coordinates with the given weight
    histogram[coord] += weight
