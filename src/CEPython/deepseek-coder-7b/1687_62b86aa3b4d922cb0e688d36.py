import re


def _validate_labels(labels):
    # Define the regular expressions for keys and values
    key_regex = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    value_regex = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')

    # Initialize an empty list to store the error messages
    errors = []

    # Iterate over the items in the labels dictionary
    for key, value in labels.items():
        # Check if the key matches the key regular expression
        if not key_regex.match(str(key)):
            errors.append({str(key): "Label key '{}' does not match the regex".format(key)})

        # Check if the value matches the value regular expression
        if isinstance(value, str) or isinstance(value, bytes):
            if not value_regex.match(value):
                errors.append({str(value): "Label value '{}' does not match the regex".format(value)})
        else:
            errors.append({str(value): 'expected string or bytes-like object'})

    # If there are any errors, raise a ValidationError
    if errors:
        raise ValidationError(errors)
