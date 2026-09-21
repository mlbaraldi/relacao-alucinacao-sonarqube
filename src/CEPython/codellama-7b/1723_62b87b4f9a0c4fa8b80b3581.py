

def scale(self, other=None, recompute=False):
    if other is None:
        if self.scale is None or recompute:
            self.scale = sum(self.histogram)
        return self.scale
    elif isinstance(other, float):
        if self.scale == 0:
            raise LenaValueError("Histograms with scale equal to zero can't be rescaled.")
        self.histogram = [other * x for x in self.histogram]
        self.scale = other * self.scale
    else:
        raise TypeError("Invalid type for argument 'other'.")
