import argparse


def parse_arguments(*arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="path to the input file")
    parser.add_argument("-o", "--output", help="path to the output file")
    parser.add_argument("-v", "--verbose", action="store_true", help="enable verbose output")
    parser.add_argument("-d", "--debug", action="store_true", help="enable debug output")
    parser.add_argument("-s", "--silent", action="store_true", help="disable all output")
    return parser.parse_args(arguments)
