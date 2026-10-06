import argparse


def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    # Create a top-level parser
    parser = argparse.ArgumentParser()

    # Create a subparsers object
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Create a global parser for arguments that are not specific to any subparser
    global_parser = argparse.ArgumentParser(add_help=False)
    global_parser.add_argument('--global_arg', help='Global argument')

    # Add the global arguments to the top-level parser
    parser.add_argument('--global_arg', help='Global argument')

    # Create subparsers
    subparser1 = subparsers.add_parser('subparser1', parents=[global_parser])
    subparser1.add_argument('--arg1', help='Argument for subparser1')

    subparser2 = subparsers.add_parser('subparser2', parents=[global_parser])
    subparser2.add_argument('--arg2', help='Argument for subparser2')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Return a dict mapping from subparser name to an argparse.Namespace instance
    return {args.subparser_name or "global": args}
