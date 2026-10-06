def validate_value(value):
    import re
    """
    Validate the given value against the corresponding regular expression.

    Args:
        value: the string to validate

    Raises:
        ValidationError: if the given value is not conform to the regular expression.
    """
    # Corresponding regular expression pattern
    regex_pattern = r'^[A-Za-z][A-Za-z0-9_-]{2,15}$'
    if not re.fullmatch(regex_pattern, value):
        raise ValidationError(f"Value '{value}' does not match the required pattern.")
