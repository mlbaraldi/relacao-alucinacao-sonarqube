

def validate_choices_args(self, args):
    """
    Check if value of choice arguments is one of the available choices.

    :param args: The received arguments.
    """
    for key, value in args.items():
        if value not in self.choices:
            raise ValueError(f'Invalid choice for argument {key}: {value}')
