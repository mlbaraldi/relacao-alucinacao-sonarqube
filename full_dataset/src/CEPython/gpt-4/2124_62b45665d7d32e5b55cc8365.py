import argparse


def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    # Create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Assume that each argument is a subparser name followed by its arguments
    for i in range(0, len(unparsed_arguments), 2):
        subparser_name = unparsed_arguments[i]
        subparser_args = unparsed_arguments[i+1].split()

        # Create the subparser
        subparser = subparsers.add_parser(subparser_name)

        # Assume that each argument is in the format --name value
        for j in range(0, len(subparser_args), 2):
            arg_name = subparser_args[j]
            subparser.add_argument(arg_name)

    # Parse the arguments
    args = parser.parse_args()

    # Return the arguments as a dict
    return {args.subparser_name: args}
