def parse_arguments(*arguments):
    import argparse
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as an ArgumentParser instance.
    """
    parser = argparse.ArgumentParser()
    # Example argument; adjust according to actual requirements
    parser.add_argument('arg', nargs='*', help="Sample argument")
    args = parser.parse_args(arguments)
    return args
