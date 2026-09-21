import argparse


def make_parsers():
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """
    # Create a top-level parser
    parser = argparse.ArgumentParser()

    # Create subparsers
    subparsers = parser.add_subparsers()

    # Create the first subparser
    subparser1 = subparsers.add_parser('subcommand1')
    subparser1.add_argument('--option1')

    # Create the second subparser
    subparser2 = subparsers.add_parser('subcommand2')
    subparser2.add_argument('--option2')

    return parser, subparser1, subparser2
