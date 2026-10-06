import argparse


def create_complex_argumet_type(self, subcommand, type_name, option_name,
                                    spec_option):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(self.option_name, type=self.spec_option, help=self.spec_option)
    parser.add_argument('--help', action='help', help='Show this help message and exit.')
    parser.add_argument('--version', action='version', version='1.0', help='Show the version and exit.')
    args, remainder = parser.parse_known_args()

    if remainder:
        raise argparse.ArgumentError(remainder)

    return args
