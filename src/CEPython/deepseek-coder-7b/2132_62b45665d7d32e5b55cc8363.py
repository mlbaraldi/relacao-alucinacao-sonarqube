import argparse


def make_parsers():
    """
    Build a top-level parser and its subparsers and return them as a tuple.
    """
    # Create the top-level parser
    parser = argparse.ArgumentParser(description='This is a top-level parser')

    # Create the subparsers
    subparsers = parser.add_subparsers(dest='command', help='sub-command help')

    # Create the parser for the 'first_command'
    parser_first_command = subparsers.add_parser('first_command', help='first command help')
    parser_first_command.add_argument('--first_option', help='first option help')

    # Create the parser for the 'second_command'
    parser_second_command = subparsers.add_parser('second_command', help='second command help')
    parser_second_command.add_argument('--second_option', help='second option help')

    return parser, subparsers

# Example usage
