

def integral(bins, edges):
    """
    Compute integral (scale for a histogram).

    *bins* contain values, and *edges* form the mesh
    for the integration.
    Their format is defined in :class:`.histogram` description.
    """

    # Check if bins and edges are lists
    if not isinstance(bins, list) or not isinstance(edges, list):
        raise ValueError("bins and edges should be lists")

    # Check if bins and edges have the same length
    if len(bins) != len(edges) - 1:
        raise ValueError("bins and edges should have the same length")

    # Check if bins and edges are sorted
    if bins != sorted(bins) or edges != sorted(edges):
        raise ValueError("bins and edges should be sorted")

    # Calculate the integral
    integral_values = [(edges[i+1] - edges[i]) * sum(bins[i] for i in range(len(bins))) for _ in bins]

    return integral_values
