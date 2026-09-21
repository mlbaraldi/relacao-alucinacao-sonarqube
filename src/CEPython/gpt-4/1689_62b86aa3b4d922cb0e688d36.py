import re
from typing import Dict, Any


def _validate_labels(labels):
    key_regex = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')
    value_regex = re.compile(r'^[a-zA-Z0-9_]*$')
    errors = []

    for key, value in labels.items():
        if not isinstance(key, str) or not key_regex.match(key):
            errors.append({str(key): f"Label key '{key}' does not match the regex {key_regex.pattern}"})
        if not isinstance(value, str) or not value_regex.match(value):
            errors.append({str(value): f"Label value '{value}' does not match the regex {value_regex.pattern}"})

    if errors:
        raise ValidationError(errors)
