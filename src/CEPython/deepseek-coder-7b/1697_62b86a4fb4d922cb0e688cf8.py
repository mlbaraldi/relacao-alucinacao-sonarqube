import re


def validate_value(value):
    """
    Validate the given value against the corresponding regular expression.

    Args:
        value: the string to validate

    Raises:
        ValueError: if the given value is not conform to the regular expression.
    """
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'

    if not re.search(email_regex, value):
        raise ValueError("Invalid email address")

# Test the function
