
def do_algebra(operator, operand):
    expression_parts = []
    for i in range(len(operator)):
        expression_parts.append(str(operand[i]))
        expression_parts.append(operator[i])
    expression_parts.append(str(operand[-1]))
    expression_str = ' '.join(expression_parts)
    return eval(expression_str)
