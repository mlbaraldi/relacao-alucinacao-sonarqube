import argparse


def parse_arguments(*arguments):
    """
    Given command-line arguments with which this script was invoked, parse the arguments and return
    them as an ArgumentParser instance.
    """
    parser = argparse.ArgumentParser()

    # Assuming arguments are in the form of ('--arg1', 'value1', '--arg2', 'value2', ...)
    for i in range(0, len(arguments), 2):
        parser.add_argument(arguments[i], type=str)

    args = parser.parse_args(arguments[1::2])

    return args
