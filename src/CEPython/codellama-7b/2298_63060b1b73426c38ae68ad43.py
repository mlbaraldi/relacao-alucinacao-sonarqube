

def extend_cli(self, root_subparsers):
    # Create a new subparser for the spec command
    spec_parser = root_subparsers.add_parser('spec', help='Generate a spec file')

    # Add arguments to the spec parser
    spec_parser.add_argument('-o', '--output', help='Output file name', required=True)
    spec_parser.add_argument('-f', '--format', help='Output file format', choices=['json', 'yaml'], required=True)
    spec_parser.add_argument('-s', '--schema', help='Schema file name', required=True)

    # Add the spec command to the root subparsers
    root_subparsers.add_parser('spec', help='Generate a spec file')
