import re


def validate_value(value):
    pattern = r"^[a-zA-Z0-9_]+$"
    if not re.match(pattern, value):
        raise ValidationError("Invalid value: {}".format(value))
