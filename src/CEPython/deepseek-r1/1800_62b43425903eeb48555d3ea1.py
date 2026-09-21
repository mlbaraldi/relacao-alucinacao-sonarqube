def _create_in_regex(self) -> Pattern:
    import re
    from typing import Pattern
    """
    Create the in-style parameter regular expression.

    Returns the compiled regular expression pattern that matches in-style parameters
    enclosed in angle brackets, optionally including a type prefix.
    """
    return re.compile(r'<(?:(?P<type>[^>:]+):)?(?P<name>[^>]+)>')
