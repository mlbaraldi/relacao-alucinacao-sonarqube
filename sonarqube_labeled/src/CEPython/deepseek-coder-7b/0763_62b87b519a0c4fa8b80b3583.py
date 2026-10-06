

def scale(self, other=None):
    if other is None:
        return self.scale
    elif all(s != 0 for s in self.scale):
        new_points = [[p[i] * other / s for i, s in enumerate(self.scale)] for p in self.points]
        return Graph(new_points, [other] * len(self.scale))
    else:
        raise ValueError("Cannot rescale graph with unknown or zero scale")
