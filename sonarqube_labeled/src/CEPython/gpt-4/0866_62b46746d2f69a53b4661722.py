

def absorb(self, args):
    new_list = []
    for expr in args:
        op, operand1, operand2 = expr
        if op == '&':
            if operand1 == operand2 or operand1 == '~' + operand2:
                new_list.append((op, operand1, operand2))
            else:
                new_list.append((op, operand1, 'B'))
        elif op == '|':
            if operand1 == operand2 or operand1 == '~' + operand2:
                new_list.append((op, operand1, operand2))
            else:
                new_list.append((op, operand1, 'B'))
    return new_list
