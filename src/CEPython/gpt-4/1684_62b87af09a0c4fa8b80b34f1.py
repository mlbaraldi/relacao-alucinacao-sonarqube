

def fill(self, coord, weight=1):
    """
    Fill histogram at *coord* with the given *weight*.

    Coordinates outside the histogram edges are ignored.
    """
    x, y = coord
    x_min, x_max, y_min, y_max = self.edges

    # Check if the coordinates are within the histogram edges
    if x_min <= x < x_max and y_min <= y < y_max:
        # Calculate the indices in the histogram for the coordinates
        x_index = int((x - x_min) / (x_max - x_min) * len(self.histogram))
        y_index = int((y - y_min) / (y_max - y_min) * len(self.histogram[0]))

        # Add the weight to the histogram at the calculated indices
        self.histogram[x_index][y_index] += weight
