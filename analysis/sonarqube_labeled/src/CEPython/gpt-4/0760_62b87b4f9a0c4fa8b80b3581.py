

def scale(self, other=None, recompute=False):
    if other is None:
        if self.scale_value is None or recompute:
            self.scale_value = sum(self.histogram)
        return self.scale_value
    else:
        if not isinstance(other, float):
            raise TypeError("other must be a float")
        if self.scale_value == 0:
            raise ValueError("Histograms with scale equal to zero can't be rescaled.")
        ratio = other / self.scale_value
        self.histogram = [value * ratio for value in self.histogram]
        self.scale_value = other  # Update the scale value
