

def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """
    integral = 0
    for i in range(len(bins)):
        integral += (edges[i+1] - edges[i]) * bins[i]
    return integral
