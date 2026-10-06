

def scale(self, other=None, recompute=False):
    if other is None:
        if self.scale is None or recompute:
            self.scale = sum(self.data.values())
        return self.scale
    elif isinstance(other, (int, float)):
        if self.scale is None or recompute:
            self.scale = sum(self.data.values())
        self.data = {k: v * other for k, v in self.data.items()}
        self.scale = None
    else:
        raise ValueError("Invalid input. Expected None or float, got " + str(type(other)))
