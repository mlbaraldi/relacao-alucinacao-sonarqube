

def validate_length_args(self, args):
    """
    Check if value of arguments is not longer than length specified.

    :param args: The received arguments.
    :param length: The specified length.
    """
    for arg in args:
        if len(arg) > length:
            return False
    return True
