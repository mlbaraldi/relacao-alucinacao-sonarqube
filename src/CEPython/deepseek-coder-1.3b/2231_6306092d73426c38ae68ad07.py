

def validate_requires_args(self, args):
    """
    Check if all the required arguments have been provided.
    """
    # Define the required arguments
    required_args = ['arg1', 'arg2', 'arg3']

    # Check if all required arguments have been provided
    for arg in required_args:
        if not getattr(args, arg, None):
            raise ValueError(f'Missing required argument: {arg}')

    # If all required arguments have been provided, return True
    return True
