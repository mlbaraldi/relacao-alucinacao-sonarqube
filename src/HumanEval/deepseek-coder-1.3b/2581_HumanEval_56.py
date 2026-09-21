

def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == "<":
            stack.append(bracket)
        else:
            if not stack or stack.pop() != "<":
                return False
    return not stack
