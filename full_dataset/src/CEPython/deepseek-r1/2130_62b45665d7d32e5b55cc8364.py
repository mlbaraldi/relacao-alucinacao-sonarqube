def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
    instance, give each requested action's subparser a shot at parsing all arguments. This allows
    common arguments like "--repository" to be shared across multiple subparsers.

    Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
    arguments, a list of remaining arguments not claimed by any subparser).
    """
    parsed = {}
    all_remaining = []
    for name, parser in subparsers.items():
        args, remaining = parser.parse_known_args(unparsed_arguments)
        parsed[name] = args
        all_remaining.append(remaining)
    
    final_remaining = []
    for arg in unparsed_arguments:
        if all(arg in remaining for remaining in all_remaining):
            final_remaining.append(arg)
    
    return (parsed, final_remaining)
