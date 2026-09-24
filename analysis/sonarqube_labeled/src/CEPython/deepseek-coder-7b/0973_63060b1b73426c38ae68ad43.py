import argparse


def extend_cli(self, root_subparsers):
    """
    Adds the spec cli options to the main entry point.

    :param subparser: the subparser object to extend.
    """
    subparser.add_argument('--option1', type=str, help='Option 1 description')
    subparser.add_argument('--option2', type=int, help='Option 2 description')
