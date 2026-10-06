import argparse


def parse_subparser_arguments(unparsed_arguments, subparsers):
    parsed_arguments = {}
    remaining_arguments = unparsed_arguments

    for subparser_name, subparser in subparsers.items():
        try:
            parsed, remaining = subparser.parse_known_args(remaining_arguments)
            parsed_arguments[subparser_name] = parsed
            remaining_arguments = remaining
        except argparse.ArgumentError:
            continue

    return parsed_arguments, remaining_arguments
