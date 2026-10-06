

def validate_min_max_args(self, args):
    """
    Check if value of arguments is between minimum and maximum values.

    :param args: The received arguments.
    """
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError("All arguments must be numbers")
        if arg < self.min_value or arg > self.max_value:
            raise ValueError(f"Argument {arg} is not within the range {self.min_value} to {self.max_value}")
    return True
