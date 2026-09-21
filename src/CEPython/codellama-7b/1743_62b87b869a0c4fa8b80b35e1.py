

def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    Convert a histogram to a graph.

    Parameters:
    - hist: The histogram to convert.
    - make_value: A function to set the value of a graph's point.
    - get_coordinate: The coordinate of a graph point created from a histogram bin.
    - field_names: The field names of the graph.
    - scale: The graph's scale.

    Returns:
    - The resulting graph.
    """
    # Check if the histogram contains only numeric bins
    if not all(isinstance(bin, (int, float)) for bin in hist):
        raise ValueError("The histogram must contain only numeric bins")

    # Check if the make_value function is defined
    if make_value is None:
        make_value = lambda bin: bin.content

    # Check if the get_coordinate parameter is valid
    if get_coordinate not in ("left", "right", "middle"):
        raise ValueError("The get_coordinate parameter must be 'left', 'right', or 'middle'")

    # Check if the field_names parameter is valid
    if not isinstance(field_names, (list, tuple)) or len(field_names) != 2:
        raise ValueError("The field_names parameter must be a list or tuple of length 2")

    # Create a new graph
    graph = Graph()

    # Set the graph's scale
    if scale is True:
        graph.scale = hist.scale
    elif scale is not None:
        graph.scale = scale

    # Iterate over the histogram's bins
    for bin in hist:
        # Get the bin's coordinate
        coordinate = get_coordinate_from_bin(bin, get_coordinate)

        # Get the bin's value
        value = make_value(bin)

        # Add a point to
