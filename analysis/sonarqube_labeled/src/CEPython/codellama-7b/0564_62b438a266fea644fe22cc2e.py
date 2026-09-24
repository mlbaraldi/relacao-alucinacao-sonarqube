import argparse


def parse_arguments(*unparsed_arguments):
    # Create an ArgumentParser instance
    parser = argparse.ArgumentParser()

    # Add subparsers for each subcommand
    subparsers = parser.add_subparsers(dest='subcommand')
    subparsers.add_parser('global', help='Global options')
    subparsers.add_parser('subcommand1', help='Subcommand 1 options')
    subparsers.add_parser('subcommand2', help='Subcommand 2 options')

    # Parse the arguments
    args = parser.parse_args(unparsed_arguments)

    # Return the parsed arguments as a dict
    return {args.subcommand: args}
