

def validate_min_max_args(self, args):
    """
    Check if value of arguments is between minimum and maximum values.

    :param args: The received arguments.
    """
    if self.min_value <= args <= self.max_value:
        return True
    else:
        return False
