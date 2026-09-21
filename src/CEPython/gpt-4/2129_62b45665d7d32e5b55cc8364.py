

def parse_subparser_arguments(unparsed_arguments, subparsers):
    parsed_arguments = {}
    remaining_arguments = unparsed_arguments[:]
    
    for subparser_name, subparser in subparsers.items():
        try:
            parsed_args, remaining_args = subparser.parse_known_args(remaining_arguments)
            parsed_arguments[subparser_name] = parsed_args
            remaining_arguments = remaining_args
        except SystemExit:
            # argparse.ArgumentParser.parse_known_args() calls sys.exit() on error.
            # We catch the exception and ignore it to allow other subparsers to try parsing the arguments.
            pass

    return parsed_arguments, remaining_arguments
