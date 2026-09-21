import os


def _resolve_string(matcher):
    """
    Get the value from environment given a matcher containing a name and an optional default value.
    If the variable is not defined in environment and no default value is provided, an Error is raised.
    """
    try:
        return os.environ[matcher['name']]
    except KeyError:
        if 'default' in matcher:
            return matcher['default']
        else:
            raise ValueError(f"Environment variable {matcher['name']} is not defined")
