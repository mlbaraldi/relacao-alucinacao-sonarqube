import argparse


def parse_arguments(*unparsed_arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as a dict mapping from subparser name (or "global") to an argparse.Namespace instance.
    """
    parser = argparse.ArgumentParser(description='Process some integers.')

    # Add subparsers
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Add subparser for "global"
    global_parser = subparsers.add_parser('global', help='Global subparser')
    global_parser.add_argument('--global_arg', type=str, help='Global argument')

    # Add subparser for "sub"
    sub_parser = subparsers.add_parser('sub', help='Subparser')
    sub_parser.add_argument('--sub_arg', type=str, help='Sub argument')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    return vars(args)
