import argparse


def make_parsers():
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """
    # Create a top-level parser
    parser = argparse.ArgumentParser()

    # Create subparsers
    subparsers = parser.add_subparsers(dest='command')

    # Create a 'start' subparser
    start_parser = subparsers.add_parser('start', help='start help')
    start_parser.add_argument('--option', help='option help')

    # Create a 'stop' subparser
    stop_parser = subparsers.add_parser('stop', help='stop help')
    stop_parser.add_argument('--option', help='option help')

    return parser, start_parser, stop_parser
