
def compare_one(a, b):
    # Convert string representations of numbers to actual numbers
    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))

    # Compare the numbers
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return None
