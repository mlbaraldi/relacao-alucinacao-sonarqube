def validate_min_max_args(self, args):
    """
    Check if value of arguments is between minimum and maximum values.

    :param args: The received arguments.
    """
    for arg in args:
        if not (arg.min <= arg.value <= arg.max):
            raise ValueError(f"Value {arg.value} is not between {arg.min} and {arg.max}.")
