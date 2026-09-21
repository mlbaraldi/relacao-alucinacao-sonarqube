def validate_length_args(self, args):
    """
    Check if value of arguments is not longer than length specified.

    :param args: The received arguments.
    """
    for arg_name, value in args.items():
        max_length = getattr(self, 'max_lengths', {}).get(arg_name)
        if max_length is not None:
            if len(value) > max_length:
                raise ValueError(f"Argument '{arg_name}' exceeds maximum length of {max_length}")
