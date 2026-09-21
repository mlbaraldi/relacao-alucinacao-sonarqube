def _resolve_string(matcher):
    import os
    """
    Resolve the environment variable value using the provided matcher which includes the variable name and optional default.
    """
    name = matcher.group(1)
    has_default = matcher.group(2) is not None
    default = matcher.group(2) if has_default else None

    if name in os.environ:
        return os.environ[name]
    elif has_default:
        return default
    else:
        raise ValueError(f"Environment variable '{name}' not found and no default provided")
