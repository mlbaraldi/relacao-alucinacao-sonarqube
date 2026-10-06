import re


def _validate_labels(labels):
    regex_dict = {
        "str": r"^[a-zA-Z0-9_]*$",
        "int": r"^-?\d+$",
        "float": r"^-?\d+\.\d+$",
        "bool": r"^(True|False)$",
        "list": r"^\[.*\]$",
        "dict": r"^\{.*\}$",
        "None": r"^None$",
    }

    errors = []

    for key, value in labels.items():
        if isinstance(key, str) and key in regex_dict:
            if not re.match(regex_dict[key], key):
                errors.append({f"'{key}'": 'Label key does not match the regex'})
        elif isinstance(value, list) and not all(isinstance(item, str) for item in value):
            errors.append({f"['{key}']": 'Expected string or bytes-like object'})
        elif isinstance(value, dict):
            for inner_key, inner_value in value.items():
                if isinstance(inner_key, str) and inner_key in regex_dict:
                    if not re.match(regex_dict[inner_key], inner_key):
                        errors.append({f"'{inner_key}'": 'Expected string or bytes-like object'})
                elif isinstance(inner_value, list) and not all(isinstance(item, str) for item in inner_value):
                    errors.append({f"['{inner_key}']": 'Expected string or bytes-like object'})
        elif isinstance(value, bool):
            if value not in [True, False]:
                errors.append({f"{value}": 'Expected string or bytes-like object'})
        elif value is None:
