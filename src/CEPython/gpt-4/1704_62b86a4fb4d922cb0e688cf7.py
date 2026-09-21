import re
from django.core.exceptions import ValidationError


def validate_key(key):
    """
    Validate the given key against the corresponding regular expression.

    Args:
        key: the string to validate

    Raises:
        ValidationError: if the given key is not conform to the regular expression.
    """
    pattern = r'^[\w]+$'  # This regex matches alphanumeric characters and underscores
    if not re.match(pattern, key):
        raise ValidationError(f"{key} is not a valid key.")
