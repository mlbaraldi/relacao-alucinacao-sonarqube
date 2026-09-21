import re
from django.core.exceptions import ValidationError


def validate_value(value):
    """
    Validate the given value against the corresponding regular expression.

    Args:
        value: the string to validate
        regex: the regular expression to validate against

    Raises:
        ValidationError: if the given value is not conform to the regular expression.
    """
    if not re.match(regex, value):
        raise ValidationError(f"{value} does not conform to the regular expression {regex}")
