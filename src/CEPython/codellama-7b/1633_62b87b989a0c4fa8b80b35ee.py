

def reset(self):
    self.histogram = {}
    if self.initial_value is not None:
        for i in range(self.num_bins):
            self.histogram[i] = self.initial_value
    else:
        self.histogram = self.make_bins()
