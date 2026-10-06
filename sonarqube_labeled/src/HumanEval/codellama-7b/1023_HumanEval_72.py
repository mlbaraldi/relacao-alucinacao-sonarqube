
def will_it_fly(q,w):
    if not is_palindromic(q):
        return False
    if sum(q) > w:
        return False
    return True

