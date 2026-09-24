

def get_silent_args(self, args):
    """
    Filter out certain arguments from a list.

    :param args: The received arguments.
    :param silent_args: The arguments to filter out.
    :return: list, filtered arguments
    """
    return [arg for arg in args if arg not in silent_args]
