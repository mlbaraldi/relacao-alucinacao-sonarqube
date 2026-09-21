

def validate_choices_args(self, args):
    """
    Check if value of choice arguments is one of the available choices.

    :param args: The received arguments.
    """
    available_choices = ['choice1', 'choice2', 'choice3']  # Define your available choices here

    for arg in args:
        if arg not in available_choices:
            raise ValueError(f"Invalid argument: {arg}. Available choices are {available_choices}")

    return True
