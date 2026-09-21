

def get_nested_custom_and_control_args(self, args):
    control_args = {}
    nested_args = {}
    custom_args = {}

    for arg in args:
        if arg.startswith("--control"):
            control_args[arg] = args[arg]
        elif arg.startswith("--nested"):
            nested_args[arg] = args[arg]
        elif arg.startswith("--custom"):
            custom_args[arg] = args[arg]

    return control_args, nested_args, custom_args
