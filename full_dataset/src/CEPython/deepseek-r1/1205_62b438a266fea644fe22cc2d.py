def parse_subparser_arguments(unparsed_arguments, subparsers):
    """
    Given a sequence of arguments and a dict from subparser name to argparse.ArgumentParser
    instance, give each requested action's subparser a shot at parsing all arguments. This allows
    common arguments like "--repository" to be shared across multiple subparsers.

    Return the result as a tuple of (a dict mapping from subparser name to a parsed namespace of
    arguments, a list of remaining arguments not claimed by any subparser).
    """
    requested_actions = []
    for arg in unparsed_arguments:
        if not arg.startswith('-') and arg in subparsers:
            requested_actions.append(arg)
    # Deduplicate while preserving order
    requested_actions = list(dict.fromkeys(requested_actions))
    
    parsed = {}
    remaining_lists = []
    
    for action in requested_actions:
        parser = subparsers[action]
        try:
            # Suppress argparse's exit behavior to handle errors gracefully
            namespace, rem = parser.parse_known_args(unparsed_arguments)
        except SystemExit:
            # Skip this subparser if parsing fails (e.g., due to missing required arguments)
            continue
        parsed[action] = namespace
        remaining_lists.append(rem)
    
    # Compute common remaining elements across all remaining lists
    common_elements = set()
    if remaining_lists:
        common_elements = set(remaining_lists[0])
        for rem in remaining_lists[1:]:
            common_elements.intersection_update(rem)
    
    # Filter original arguments to retain order, including only those in common_elements
    final_remaining = [arg for arg in unparsed_arguments if arg in common_elements]
    
    return (parsed, final_remaining)
