from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    from typing import List
    # Remove all spaces from the input string
    s = paren_string.replace(' ', '')
    result = []
    current_group = []
    balance = 0
    
    for char in s:
        current_group.append(char)
        if char == '(':
            balance += 1
        else:
            balance -= 1
        
        if balance == 0:
            result.append(''.join(current_group))
            current_group = []
    
    return result
