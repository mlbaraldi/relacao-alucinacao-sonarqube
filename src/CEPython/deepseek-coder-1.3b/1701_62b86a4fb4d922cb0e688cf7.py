import re


def validate_key(key):
    """
    Validate the given key against the corresponding regular expression.

    Args:
        key: the string to validate

    Raises:
        ValidationError: if the given key is not conform to the regular expression.
    """
    # Define the regular expression for a key
    regex = r'^[a-zA-Z0-9_]+$'

    # Validate the key
    if not re.match(regex, key):
        raise ValidationError('Invalid key. It should only contain letters, numbers, and underscores.')
