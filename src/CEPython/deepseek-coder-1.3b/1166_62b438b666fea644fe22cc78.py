import argparse


def parse_arguments(*arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as an ArgumentParser instance.
    """
    parser = argparse.ArgumentParser(description='Parse command-line arguments.')

    # Add arguments here
    parser.add_argument('--arg1', type=str, help='Argument 1 help')
    parser.add_argument('--arg2', type=int, help='Argument 2 help')
    parser.add_argument('--arg3', action='store_true', help='Argument 3 help')

    return parser.parse_args()
