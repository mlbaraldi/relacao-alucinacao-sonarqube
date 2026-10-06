

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.
    """
    balance = 0
    for b in brackets:
        if b == '<':
            balance += 1
        else:
            if balance == 0:
                return False
            balance -= 1
    return balance == 0
