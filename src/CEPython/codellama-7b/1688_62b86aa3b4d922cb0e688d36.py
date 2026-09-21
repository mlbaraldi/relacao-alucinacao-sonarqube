import re


def _validate_labels(labels):
    """
    Check that keys and values in the given labels match against their corresponding
    regular expressions.

    Args:
        labels (dict): the different labels to validate.

    Raises:
        ValidationError: if any of the keys and labels does not match their respective
            regular expression. The error contains as message the list of all errors
            which occurred in the labels. Each element of the list is a dictionary with
            one key-value pair:
            - key: the label key or label value for which an error occurred as string.
            - value: the error message.

            .. code:: python

                # Example:
                labels = {
                    "key1": "valid",
                    "key2": ["invalid"],
                    "$$": "invalid",
                    True: True,
                }
                try:
                    _validate_labels(labels)
                except ValidationError as err:
                    assert err.messages == [
                        {"['invalid']": 'expected string or bytes-like object'},
                        {'$$': "Label key '$$' does not match the regex [...]"},
                        {'True': 'expected string or bytes-like object'},
                        {'True': 'expected string or bytes-like object'},
                    ]
    """
    errors = []
    for key, value in labels.items():
        if not re.match(r'^[a-zA-Z0-9_]+$', key):
            errors.append({'key': key, 'value': f"Label key '{key}' does not match the regex [...]"})
        if not isinstance(value, str) and not isinstance(value, bytes):
            errors.append({'key': key, 'value': f"Label value '{value}' does not match the regex [...]"})
    if errors:
        raise ValidationError(errors)
