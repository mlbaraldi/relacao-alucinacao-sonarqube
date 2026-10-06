import re


def validate_value(value):
    """
    Validate the given value against the corresponding regular expression.

    Args:
        value: the string to validate

    Raises:
        ValidationError: if the given value is not conform to the regular expression.
    """
    # Define the regular expression for the value
    regex = r'^[a-zA-Z0-9_]+$'

    # Check if the value matches the regular expression
    if not re.match(regex, value):
        raise ValidationError('Invalid value')
