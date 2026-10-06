

def extend_cli(self, root_subparsers):
    """
    Adds the spec cli options to to the main entry point.

    :param root_subparsers: the subparser object to extend.
    """
    # Assuming that the spec cli options are stored in a dictionary
    spec_cli_options = {
        'option1': {
            'help': 'Description for option1',
            'type': str,
            'default': None
        },
        'option2': {
            'help': 'Description for option2',
            'type': int,
            'default': 0
        },
        # Add more options as needed
    }

    # Create a new subparser for the spec cli options
    spec_parser = root_subparsers.add_parser('spec', help='spec cli options')

    # Add the spec cli options to the new subparser
    for option, attributes in spec_cli_options.items():
        spec_parser.add_argument('--' + option, help=attributes['help'], type=attributes['type'], default=attributes['default'])
