

def validate_length_args(self, args):
    """
    Check if value of arguments is not longer than length specified.

    :param args: The received arguments.
    """
    for arg in args:
        if len(arg) > 10:
            raise ValueError("Argument is longer than the specified length (10)")
    return True
