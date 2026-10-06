import re
from typing import Set, Tuple


def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    """
    Find tags in text.

    Tries to ignore tags inside code blocks.

    Optionally, if passed a "replacer", will also replace the tag word with the result
    of the replacer function called with the tag word.

    Returns a set of tags and the original or replaced text.
    """
    # Define a regular expression pattern for matching tags
    tag_pattern = re.compile(r'<([^>]+)>')
    
    # Function to replace tags with the result of the replacer function
    def replace_tag(match):
        tag = match.group(1)
        if replacer:
            return replacer(tag)
        return tag
    
    # Function to ignore tags inside code blocks
    def ignore_tags_in_code_blocks(text):
        # Define a regular expression pattern for matching code blocks
        code_block_pattern = re.compile(r'```(.*?)```', re.DOTALL)
        return code_block_pattern.sub(lambda m: ignore_tags_in_code_blocks(m.group(1)), text)
    
    # Find all tags in the text
    tags = set(tag_pattern.findall(text))
    
    # Replace tags if a replacer function is provided
    if replacer:
        text = tag_pattern.sub(replace_tag, text)
    
    # Ignore tags inside code blocks
    text = ignore_tags_in_code_blocks(text)
    
    return tags, text

# Example usage:
