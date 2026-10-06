from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the current character is an opening parenthesis, add it to the current group
        if char == '(':
            current_group = char
        # If the current character is a closing parenthesis, add it to the current group
        elif char == ')':
            current_group += char
        # If the current character is a space, ignore it
        elif char == ' ':
            continue
        # If the current character is anything else, raise an error
        else:
            raise ValueError(f"Invalid character '{char}' in input string")

        # If the current group is not empty, add it to the list of separated groups
        if current_group:
            separated_groups.append(current_group)

    return separated_groups
