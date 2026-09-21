

def extend_cli(self, root_subparsers):
    """
    Adds the spec cli options to to the main entry point.

    :param subparser: the subparser object to extend.
    """

    # Add the spec cli options to the main entry point
    root_subparsers.add_parser('spec', help='Show the spec file')

    # Add the version cli option to the main entry point
    root_subparsers.add_parser('version', help='Show the version of the program')

    # Add the help cli option to the main entry point
    root_subparsers.add_parser('help', help='Show the help message')
