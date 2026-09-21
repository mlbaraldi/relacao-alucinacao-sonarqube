
def compare_one(a, b):
    if a == b:
        return None
    elif isinstance(a, int) and isinstance(b, float):
        return b
    elif isinstance(a, float) and isinstance(b, int):
        return a
    elif isinstance(a, str) and isinstance(b, str):
        if a.replace(",", ".") > b.replace(",", "."):
            return a
        else:
            return b
    else:
        raise ValueError("Invalid input types")
