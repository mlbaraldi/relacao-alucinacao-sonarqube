import matplotlib.pyplot as plt


def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    # Check if make_value is a function
    if make_value and not callable(make_value):
        raise ValueError("make_value must be a function")

    # Create a new figure and axis
    fig, ax = plt.subplots()

    # Convert the histogram to a list of tuples
    # Each tuple represents a point in the graph
    points = [(getattr(bin, field_names[0]), getattr(bin, field_names[1])) for bin in hist]

    # If make_value is not None, use it to set the values of the points
    if make_value:
        points = [(x, make_value(y)) for (x, y) in points]

    # If scale is True, use the scale of the histogram
    if scale is True:
        scale = hist.scale
    # Otherwise, use the default scale
    else:
        scale = hist.default_scale

    # Plot the points
    ax.bar(
        [x[0] for x in points],
        [x[1] for x in points],
        width=scale,
        align=get_coordinate
    )

    # Set the labels and title of the graph
    ax.set_xlabel(field_names[0])
    ax.set_ylabel(field_names[1])
    ax.set_title("Histogram to Graph")

    # Return the figure
    return fig
