import argparse


def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    parser = argparse.ArgumentParser(description='Process some integers.')
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Define subparsers here
    subparser1 = subparsers.add_parser('subparser1')
    subparser1.add_argument('--arg1', type=int, help='arg1 description')
    subparser1.add_argument('--arg2', type=str, help='arg2 description')

    subparser2 = subparsers.add_parser('subparser2')
    subparser2.add_argument('--arg3', type=float, help='arg3 description')
    subparser2.add_argument('--arg4', type=str, help='arg4 description')

    # Parse arguments
    args = parser.parse_args(unparsed_arguments[0])

    # Return arguments as a dict
    return vars(args)
