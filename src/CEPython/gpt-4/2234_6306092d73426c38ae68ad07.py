

def validate_requires_args(self, args):
    """
    Check if all the required arguments have been provided.
    """
    required_args = ['arg1', 'arg2', 'arg3']  # list of required arguments

    for arg in required_args:
        if arg not in args:
            return False

    return True
