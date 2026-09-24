import re
from typing import Tuple, Set


def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    """
    Find tags in text.

    Tries to ignore tags inside code blocks.

    Optionally, if passed a "replacer", will also replace the tag word with the result
    of the replacer function called with the tag word.

    Returns a set of tags and the original or replaced text.
    """

    # Regular expression pattern for finding tags
    pattern = r'<[^>]*>'

    # Find all tags in the text
    tags = set(re.findall(pattern, text))

    # If a replacer function was provided, replace the tags
    if replacer:
        for tag in tags:
            text = text.replace(tag, replacer(tag))

    return tags, text
