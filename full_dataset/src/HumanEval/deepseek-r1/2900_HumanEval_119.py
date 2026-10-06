
def match_parens(lst):
    def is_balanced(s):
        balance = 0
        for char in s:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0
    
    s1, s2 = lst[0], lst[1]
    total_open = s1.count('(') + s2.count('(')
    total_close = s1.count(')') + s2.count(')')
    
    if total_open != total_close:
        return 'No'
    
    option1 = s1 + s2
    option2 = s2 + s1
    
    if is_balanced(option1) or is_balanced(option2):
        return 'Yes'
    else:
        return 'No'
