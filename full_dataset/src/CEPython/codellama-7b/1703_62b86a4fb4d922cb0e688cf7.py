import re


def validate_key(key):
    pattern = r"^[a-zA-Z0-9_-]+$"
    if not re.match(pattern, key):
        raise ValidationError("Invalid key: {}".format(key))
