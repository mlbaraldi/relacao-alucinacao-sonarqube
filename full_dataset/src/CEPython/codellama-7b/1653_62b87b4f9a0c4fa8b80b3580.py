

def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    # Initialize the integral to zero
    integral = 0

    # Loop over the bins
    for i in range(len(bins)):
        # Get the bin value and the left and right edges
        bin_value = bins[i]
        left_edge = edges[i]
        right_edge = edges[i + 1]

        # Compute the bin width
        bin_width = right_edge - left_edge

        # Add the bin value times the bin width to the integral
        integral += bin_value * bin_width

    # Return the integral
    return integral
