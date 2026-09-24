

def scale(self, other=None, recompute=False):
    if other is None:
        if self.scale is None or recompute:
            self.compute_scale()
        return self.scale
    elif isinstance(other, (int, float)):
        if self.scale == 0:
            raise ValueError("Histogram with scale equal to zero can't be rescaled.")
        self.data = [int(val * other / self.scale) for val in self.data]
        self.scale = other
        return self.data
    else:
        raise TypeError("Invalid type for rescaling. Expected int or float.")
