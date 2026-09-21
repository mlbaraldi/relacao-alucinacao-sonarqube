

def scale(self, other=None):
    if other is None:
        return self.scale
    else:
        if self.scale == 0 or self.scale is None:
            raise LenaValueError("Cannot rescale graph with unknown or zero scale")
        self.scale = other
