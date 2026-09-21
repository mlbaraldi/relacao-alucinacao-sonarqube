

def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_: bin_

    if get_coordinate == "left":
        coordinates = range(len(hist))
    elif get_coordinate == "right":
        coordinates = range(len(hist) + 1, 0, -1)
    elif get_coordinate == "middle":
        coordinates = [(i + 1) / 2 for i in range(len(hist))]
    else:
        raise ValueError("Invalid get_coordinate value")

    if scale is True:
        scale = hist.scale

    graph = []
    for i, bin_ in enumerate(hist):
        value = make_value(bin_)
        if isinstance(value, tuple):
            point = dict(zip(field_names, value))
        else:
            point = {field_names[0]: value}
        point["x"] = coordinates[i]
        if scale is not None:
            point["x"] *= scale
        graph.append(point)

    return graph
