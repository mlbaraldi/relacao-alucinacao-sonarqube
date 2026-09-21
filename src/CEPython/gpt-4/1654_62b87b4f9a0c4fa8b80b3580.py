

def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    # Check if bins and edges have compatible lengths
    if len(bins) != len(edges) - 1:
        raise ValueError("Length of bins must be one less than length of edges")

    # Compute the integral as the sum of the areas of the rectangles
    integral = 0
    for i in range(len(bins)):
        width = edges[i+1] - edges[i]
        height = bins[i]
        area = width * height
        integral += area

    return integral
