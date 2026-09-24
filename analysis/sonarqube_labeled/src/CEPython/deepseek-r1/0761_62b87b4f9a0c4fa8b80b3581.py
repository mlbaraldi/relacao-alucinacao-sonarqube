def scale(self, other=None, recompute=False):
    """
    Compute or set scale (integral of the histogram).

    If *other* is ``None``, return scale of this histogram.
    If its scale was not computed before,
    it is computed and stored for subsequent use
    (unless explicitly asked to *recompute*).
    Note that after changing (filling) the histogram
    one must explicitly recompute the scale
    if it was computed before.

    If a float *other* is provided, rescale self to *other*.

    Histograms with scale equal to zero can't be rescaled.
    :exc:`.LenaValueError` is raised if one tries to do that.
    """
    if other is None:
        # Compute or return the current scale
        if recompute or not hasattr(self, '_scale') or self._scale is None:
            # Calculate the integral of the histogram
            total = 0.0
            for bin in self.bins:
                total += bin.value * bin.volume
            self._scale = total
        return self._scale
    else:
        # Rescale the histogram to the new scale 'other'
        if not isinstance(other, (float, int)):
            raise TypeError("other must be a float")
        other_float = float(other)
        current_scale = self.scale(recompute=recompute)
        if current_scale == 0:
            raise LenaValueError("Cannot rescale histogram with zero scale")
        factor = other_float / current_scale
        for bin in self.bins:
            bin.value *= factor
        self._scale = other_float
