def fill(self, coord, weight=1):
    import bisect
    """
    Fill histogram at *coord* with the given *weight*.

    Coordinates outside the histogram edges are ignored.
    """
    # Check if all coordinates are within the edges
    for i in range(len(coord)):
        axis_edges = self.edges[i]
        c = coord[i]
        if c < axis_edges[0] or c >= axis_edges[-1]:
            return

    # Compute the indices for each axis
    indices = []
    for i in range(len(coord)):
        axis_edges = self.edges[i]
        c = coord[i]
        idx = bisect.bisect_right(axis_edges, c) - 1
        indices.append(idx)

    # Update the corresponding bin in the data array
    # For a 2D histogram, access as data[i][j]
    # For higher dimensions, generalize accordingly
    try:
        current = self.data
        for index in indices[:-1]:
            current = current[index]
        current[indices[-1]] += weight
    except IndexError:
        # Handle cases where indices are out of bounds (though checks should prevent this)
        pass
