import re
from typing import Pattern


def _create_in_regex(self) -> Pattern:
    """
    Create the in-style parameter regular expression.

    Returns the in-style parameter regular expression (:class:`re.Pattern`).
    """
    in_style_regex = r'\:in\((.*?)\)'
    return re.compile(in_style_regex)
