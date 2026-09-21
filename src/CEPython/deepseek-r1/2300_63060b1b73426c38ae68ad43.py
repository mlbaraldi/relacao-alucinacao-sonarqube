def extend_cli(self, root_subparsers):
    """
    Adds the spec cli options to the main entry point.

    :param root_subparsers: the subparser object to extend.
    """
    spec_parser = root_subparsers.add_parser('spec', help='Manage specifications')
    spec_parser.add_argument('--input', help='Input file or directory for spec processing')
    spec_parser.add_argument('--output', help='Output path for generated spec files')
    spec_parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
