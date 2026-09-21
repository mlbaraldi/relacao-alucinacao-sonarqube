

def fill(self, coord, weight=1):
    if coord < 0 or coord >= len(self.bins):
        return
    self.hist[coord] += weight
