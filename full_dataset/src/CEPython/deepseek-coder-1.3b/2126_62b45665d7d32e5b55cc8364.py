

def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
    instance, give each requested action's subparser a shot at parsing all arguments. This allows
    common arguments like "--repository" to be shared across multiple subparsers.

    Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
    arguments, a list of remaining arguments not claimed by any subparser).
    """

    parsed_args = {}
    remaining_args = []

    for subparser_name, subparser in subparsers.items():
        parsed_args[subparser_name] = subparser.parse_args(unparsed_arguments)

    remaining_args = [arg for arg in unparsed_arguments if arg not in {arg.arg for subparser in subparsers.values() for arg in subparser.parse_args([])._positionals}]

    return parsed_args, remaining_args
