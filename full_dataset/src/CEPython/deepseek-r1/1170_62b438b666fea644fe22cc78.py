def parse_arguments(*arguments):
    import argparse
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as an ArgumentParser instance.
    """
    parser = argparse.ArgumentParser()
    parser.parse_args(arguments)
    return parser
