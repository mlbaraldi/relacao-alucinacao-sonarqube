

def get_silent_args(self, args):
    """
    List of silent argument names.

    :param args: The received arguments.
    :return: List, silent argument names.
    """
    silent_args = []
    for arg in args:
        if arg.startswith('-'):
            silent_args.append(arg[1:])
    return silent_args
