import re
from typing import Set, Tuple, Callable


def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    # Regular expression to find tags
    tag_pattern = re.compile(r'\B#\w+\b', re.IGNORECASE)

    # Regular expression to find code blocks
    code_block_pattern = re.compile(r'```.*?```', re.DOTALL)

    # Remove code blocks from the text
    text_without_code_blocks = re.sub(code_block_pattern, '', text)

    # Find all tags in the text
    tags = set(re.findall(tag_pattern, text_without_code_blocks))

    # If a replacer function is provided, replace the tags in the text
    if replacer is not None:
        for tag in tags:
            text = text.replace(tag, replacer(tag))

    return tags, text
