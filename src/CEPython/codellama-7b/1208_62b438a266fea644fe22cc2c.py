import argparse


def make_parsers():
    # Create the top-level parser
    parser = argparse.ArgumentParser(description='My program')

    # Create subparsers
    subparsers = parser.add_subparsers(help='sub-command help')

    # Create a parser for the "foo" subcommand
    foo_parser = subparsers.add_parser('foo', help='foo help')
    foo_parser.add_argument('--bar', help='bar help')

    # Create a parser for the "baz" subcommand
    baz_parser = subparsers.add_parser('baz', help='baz help')
    baz_parser.add_argument('--qux', help='qux help')

    return parser, subparsers
