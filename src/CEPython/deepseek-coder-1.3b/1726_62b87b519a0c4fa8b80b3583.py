

def scale(self, other=None):
    if other is None:
        # If no other value is provided, return the scale of this graph
        return max(max(self.data, key=abs))
    else:
        # If a numeric other value is provided, rescale to that value
        return [(x / other) for x in self.data[0]]
