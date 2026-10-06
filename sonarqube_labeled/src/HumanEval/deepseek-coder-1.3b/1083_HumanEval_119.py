
def match_parens(lst):
    s = ''.join(lst)
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return 'No'
            stack.pop()
    return 'Yes' if not stack else 'No'
