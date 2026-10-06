def get_silent_args(self, args):
    """
    list of silenced argument

    :param args: The received arguments.
    :return: list, silenced argument names
    """
    return [key for key, value in vars(args).items() if value is False]
