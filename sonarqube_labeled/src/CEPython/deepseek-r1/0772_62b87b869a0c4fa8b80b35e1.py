def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if get_coordinate not in ('left', 'right', 'middle'):
        raise ValueError(f"Invalid get_coordinate: {get_coordinate}")

    if len(hist.axes) != 1:
        raise ValueError("hist_to_graph requires a 1D histogram")
    
    axis = hist.axes[0]
    edges = axis.edges
    num_bins = len(edges) - 1

    points = []
    for i in range(num_bins):
        left = edges[i]
        right = edges[i + 1]
        if get_coordinate == 'left':
            x = left
        elif get_coordinate == 'right':
            x = right
        else:
            x = (left + right) / 2

        bin_content = hist.bins[i]
        if make_value is None:
            value = bin_content
        else:
            value = make_value(bin_content)

        if isinstance(value, tuple):
            point = (x,) + value
        else:
            point = (x, value)
        points.append(point)

    graph_scale = hist.scale if scale is True else scale

    return Graph(points=points, field_names=field_names, scale=graph_scale)
