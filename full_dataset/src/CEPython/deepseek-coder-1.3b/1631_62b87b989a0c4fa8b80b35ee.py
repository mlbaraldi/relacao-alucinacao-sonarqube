

def reset(self):
    """
    Reset the histogram.

    Current context is reset to an empty dict.
    Bins are reinitialized with the *initial_value*
    or with *make_bins()* (depending on the initialization).
    """
    self.histogram = {}
