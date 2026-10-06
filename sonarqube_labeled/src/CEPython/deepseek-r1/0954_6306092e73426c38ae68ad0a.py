def validate_choices_args(self, args):
    """
    Check if value of choice arguments is one of the available choices.

    :param args: The received arguments.
    """
    for action in self._actions:
        if action.choices is not None:
            value = getattr(args, action.dest)
            if value not in action.choices:
                raise ValueError(f"Invalid choice '{value}' for argument '{action.dest}'. Choices are: {action.choices}")
