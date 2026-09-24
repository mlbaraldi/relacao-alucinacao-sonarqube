def scale(self, other=None):
    from lena.core import LenaValueError
    """
    Get or set the scale of the graph.

    If *other* is ``None``, return the scale of this graph.

    If a numeric *other* is provided, rescale to that value.
    If the graph has unknown or zero scale,
    rescaling that will raise :exc:`~.LenaValueError`.

    To get meaningful results, graph's fields are used.
    Only the last coordinate is rescaled.
    For example, if the graph has *x* and *y* coordinates,
    then *y* will be rescaled, and for a 3-dimensional graph
    *z* will be rescaled.
    All errors are rescaled together with their coordinate.
    """
    if other is None:
        return self._scale
    else:
        if not isinstance(other, (int, float)):
            raise TypeError("Scale must be a numeric value.")
        current_scale = self._scale
        if current_scale is None or current_scale == 0:
            raise LenaValueError("Cannot rescale graph with unknown or zero scale.")
        factor = other / current_scale
        for point in self.points:
            # Assuming each point's last coordinate and its error are the last two elements
            point[-2] *= factor
            point[-1] *= factor
        self._scale = other
