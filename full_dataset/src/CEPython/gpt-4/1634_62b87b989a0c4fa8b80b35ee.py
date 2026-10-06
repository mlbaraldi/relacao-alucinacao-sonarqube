

def reset(self):
    """
    Reset the histogram.

    Current context is reset to an empty dict.
    Bins are reinitialized with the *initial_value*
    or with *make_bins()* (depending on the initialization).
    """
    self.context = {}
    if hasattr(self, 'initial_value'):
        self.bins = [self.initial_value for _ in range(len(self.bins))]
    elif hasattr(self, 'make_bins'):
        self.bins = self.make_bins()
    else:
        self.bins = []
