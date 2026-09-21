def validate_arg_deprecation(self, cli_args, answer_file_args):
    """
    Validates and prints the deprecated arguments.

    :param cli_args: the dict of arguments from cli
    :param answer_file_args:  the dict of arguments from files
    """
    # Check each argument in CLI arguments
    for arg in cli_args:
        if arg in self.deprecated_args:
            print(f"Deprecated argument '{arg}' found in CLI arguments.")
    
    # Check each argument in answer file arguments
    for arg in answer_file_args:
        if arg in self.deprecated_args:
            print(f"Deprecated argument '{arg}' found in answer file arguments.")
