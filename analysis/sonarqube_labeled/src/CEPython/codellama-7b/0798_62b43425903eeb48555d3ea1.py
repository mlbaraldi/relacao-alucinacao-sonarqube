import re


def _create_in_regex(self) -> Pattern:
    # Create a regular expression that matches the in-style parameter
    # syntax, which is of the form "in:<parameter_name>"
    regex = re.compile(r"in:(\w+)")
    return regex
