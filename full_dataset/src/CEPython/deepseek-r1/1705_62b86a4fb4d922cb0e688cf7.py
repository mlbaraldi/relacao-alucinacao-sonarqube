def validate_key(key):
    import re
    """
    Validate the given key against the corresponding regular expression.

    Args:
        key: the string to validate

    Raises:
        ValidationError: if the given key is not conform to the regular expression.
    """
    # Replace this regular expression with the actual one required for your use case
    pattern = r'^[A-Za-z0-9_]+$'
    if not re.fullmatch(pattern, key):
        raise ValidationError(f"Invalid key format: {key}")
