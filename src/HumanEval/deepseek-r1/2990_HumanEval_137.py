
def compare_one(a, b):
    def parse(var):
        if isinstance(var, str):
            return float(var.replace(',', '.'))
        return float(var)
    
    a_val = parse(a)
    b_val = parse(b)
    
    if a_val == b_val:
        return None
    return a if a_val > b_val else b
