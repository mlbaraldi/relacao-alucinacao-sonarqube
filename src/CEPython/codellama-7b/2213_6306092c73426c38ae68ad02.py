

def validate_arg_deprecation(self, cli_args, answer_file_args):
    # Get the list of deprecated arguments
    deprecated_args = self.get_deprecated_args()

    # Check if any of the arguments in the CLI args are deprecated
    for arg in cli_args:
        if arg in deprecated_args:
            print(f"Warning: The {arg} argument is deprecated and will be removed in a future version. Please use {deprecated_args[arg]} instead.")

    # Check if any of the arguments in the answer file args are deprecated
    for arg in answer_file_args:
        if arg in deprecated_args:
            print(f"Warning: The {arg} argument is deprecated and will be removed in a future version. Please use {deprecated_args[arg]} instead.")
