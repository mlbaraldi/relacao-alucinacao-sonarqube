import re


def _resolve_string(matcher):
    name = matcher.group(1)
    default = matcher.group(2)
    value = os.environ.get(name)
    if value is None and default is None:
        raise ValueError(f"Environment variable {name} is not defined")
    return value or default
