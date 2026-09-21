

def absorb(self, args):
    """
    Given an `args` sequence of expressions, return a new list of expression
    applying absorption and negative absorption.

    See https://en.wikipedia.org/wiki/Absorption_law

    Absorption::

        A & (A | B) = A, A | (A & B) = A

    Negative absorption::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    new_list = []
    for arg in args:
        if "&" in arg:
            left, right = arg.split("&")
            new_list.append(left)
            new_list.append(right)
        elif "|" in arg:
            left, right = arg.split("|")
            new_list.append(left)
            new_list.append(right)
        elif "~" in arg:
            left = arg.split("~")[0]
            new_list.append(left)
            new_list.append("~" + left)
        else:
            new_list.append(arg)
    return new_list
