import re


def validate_key(key):
    """
    Validate the given key against the regular expression.

    Args:
        key: the string to validate

    Raises:
        ValueError: if the given key is not conform to the regular expression.
    """
    pattern = re.compile(r'^[a-zA-Z0-9]{5,10}$')
    if not pattern.match(key):
        raise ValueError('Invalid key')

# Example usage:
