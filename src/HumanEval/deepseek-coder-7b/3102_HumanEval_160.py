
def do_algebra(operator, operand):
    # Initialize the result with the first operand
    result = operand[0]

    # Iterate over the operator list
    for i in range(len(operator)):
        # Perform the operation and update the result
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]

    return result
