

def absorb(self, args):
    new_list = []
    for expr in self.args:
        if '|' in expr:
            new_expr = self.apply_absorption(expr)
            new_expr = self.apply_negative_absorption(new_expr)
            new_list.append(new_expr)
    return new_list
