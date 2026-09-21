import argparse


def parse_subparser_arguments(unparsed_arguments, subparsers):
    # Create a new argument parser that will be used to parse the arguments
    # for each subparser.
    parser = argparse.ArgumentParser()

    # Add the common arguments to the parser.
    parser.add_argument("--repository", help="The repository to use")

    # Add the subparsers to the parser.
    for name, subparser in subparsers.items():
        parser.add_argument(f"--{name}", help=f"Use the {name} subparser")

    # Parse the arguments using the parser.
    args = parser.parse_args(unparsed_arguments)

    # Create a dictionary to map the subparser name to the parsed arguments.
    parsed_args = {}

    # Iterate over the subparsers and their corresponding arguments.
    for name, subparser in subparsers.items():
        # If the subparser was selected, parse the arguments using the subparser.
        if args[f"--{name}"]:
            parsed_args[name] = subparser.parse_args(args[f"--{name}"])

    # Return the parsed arguments and the remaining arguments.
    return parsed_args, args[f"--{name}"]
