

def validate_min_max_args(self, args):
    for arg in args:
        if arg < self.min_value or arg > self.max_value:
            raise ValueError(f"Invalid argument value: {arg}")
