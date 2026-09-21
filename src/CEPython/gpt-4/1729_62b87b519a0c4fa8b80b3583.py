

def scale(self, other=None):
    if other is None:
        return self.scale
    elif isinstance(other, (int, float)):
        if self.scale == 0:
            raise ValueError("Graph has unknown or zero scale, rescaling not possible.")
        else:
            for coordinate in self.coordinates:
                coordinate[-1] *= other / self.scale
            self.scale = other
    else:
        raise TypeError("Scale value must be a number.")
