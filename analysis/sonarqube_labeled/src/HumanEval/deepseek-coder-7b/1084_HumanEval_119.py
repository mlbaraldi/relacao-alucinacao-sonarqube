
def match_parens(lst):
    s1, s2 = lst[0], lst[1]
    if s1.count('(') != s1.count(')'):
        return 'No'
    if s2.count('(') != s2.count(')'):
        return 'No'
    if s1.count('(') + s2.count('(') != s1.count(')') + s2.count(')'):
        return 'No'
    return 'Yes'
