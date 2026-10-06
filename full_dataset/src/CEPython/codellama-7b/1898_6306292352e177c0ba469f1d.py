import re


def find_tags(text: str, replacer: callable = None) -> Tuple[Set, str]:
    tags = set()
    replaced_text = text

    # Find tags inside code blocks
    code_blocks = re.findall(r'```(.*?)```', text)
    for code_block in code_blocks:
        replaced_text = replaced_text.replace(code_block, "")

    # Find tags outside code blocks
    tags = re.findall(r"#\w+", replaced_text)

    # Replace tags with the result of the replacer function
    if replacer:
        replaced_text = re.sub(r"#\w+", lambda x: replacer(x.group(0)), replaced_text)

    return tags, replaced_text
