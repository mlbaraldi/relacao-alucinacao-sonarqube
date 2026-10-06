from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Input: A string representing multiple groups of nested parentheses separated by spaces.
    Output: A list of integers representing the deepest level of nesting of parentheses for each group.
    """
    # Initialize an empty list to store the results
    results = []

    # Iterate over the groups of parentheses in the input string
    for group in paren_string.split(' '):
        # Initialize a counter to keep track of the current level of nesting
        level = 0

        # Iterate over the characters in the current group
        for char in group:
            # If the character is an opening parenthesis, increment the level
            if char == '(':
                level += 1
            # If the character is a closing parenthesis, decrement the level
            elif char == ')':
                level -= 1

        # Add the current level of nesting to the results list
        results.append(level)

    return results
