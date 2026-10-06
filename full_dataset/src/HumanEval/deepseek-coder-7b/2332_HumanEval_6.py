from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    depths = []
    for group in paren_string.split():
        depth = 0
        max_depth = 0
        stack = []
        for char in group:
            if char == '(':
                depth += 1
                stack.append(char)
            elif char == ')':
                depth -= 1
                stack.pop()
            max_depth = max(max_depth, depth)
        depths.append(max_depth)
    return depths
