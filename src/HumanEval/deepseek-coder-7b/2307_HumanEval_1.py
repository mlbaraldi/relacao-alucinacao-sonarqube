from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    stack = []
    groups = []
    current_group = ''

    for char in paren_string:
        if char == '(':
            if current_group:
                stack.append(current_group)
                current_group = ''
            stack.append(char)
        elif char == ')':
            if not stack or stack[-1] != '(':
                return []
            stack.pop()
            current_group += ')'
            if not stack:
                groups.append(current_group)
                current_group = ''
        else:
            continue

    return groups

