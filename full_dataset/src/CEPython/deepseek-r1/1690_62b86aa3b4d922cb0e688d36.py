def _validate_labels(labels):
    import re
    """
    Check that keys and values in the given labels match against their corresponding
    regular expressions.

    Args:
        labels (dict): the different labels to validate.

    Raises:
        ValidationError: if any of the keys and labels does not match their respective
            regular expression. The error contains as message the list of all errors
            which occurred in the labels.
    """
    errors = []
    # Regular expression patterns for validation
    KEY_REGEX = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    VALUE_REGEX = re.compile(r'^[a-zA-Z0-9_]*$')  # Adjust regex as necessary

    for key, value in labels.items():
        # Validate key
        if not isinstance(key, str):
            errors.append({str(key): 'expected string or bytes-like object'})
        else:
            if not KEY_REGEX.match(key):
                errors.append({key: f"Label key '{key}' does not match the required format."})
        
        # Validate value
        if not isinstance(value, str):
            errors.append({str(value): 'expected string or bytes-like object'})
        else:
            if not VALUE_REGEX.match(value):
                errors.append({value: f"Label value '{value}' does not match the required format."})
    
    if errors:
        raise ValidationError(errors)
