
def compare_one(a, b):
    # Convert strings to floats if necessary
    a_val = float(a.replace(',', '.')) if isinstance(a, str) else a
    b_val = float(b.replace(',', '.')) if isinstance(b, str) else b

    # Compare the values
    if a_val > b_val:
        return a
    elif a_val < b_val:
        return b
    else:
        return None
