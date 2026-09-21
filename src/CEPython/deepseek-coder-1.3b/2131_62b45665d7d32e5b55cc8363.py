import argparse


def make_parsers():
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """

    # Create the top-level parser
    parser = argparse.ArgumentParser(description='Top-level parser')

    # Add subparsers
    subparsers = parser.add_subparsers(dest='subparser_name')

    # Create subparsers
    subparser1 = subparsers.add_parser('subparser1', description='Subparser 1')
    subparser2 = subparsers.add_parser('subparser2', description='Subparser 2')

    # Return the parsers as a tuple
    return parser, subparser1, subparser2
