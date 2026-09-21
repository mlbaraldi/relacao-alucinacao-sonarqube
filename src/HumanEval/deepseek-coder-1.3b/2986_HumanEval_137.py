
def compare_one(a, b):
    try:
        if isinstance(a, str) and isinstance(b, str):
            if '.' in a or ',' in a:
                a = float(a.replace(',', '.'))
            if '.' in b or ',' in b:
                b = float(b.replace(',', '.'))
            return max(a, b)
        else:
            return max(a, b)
    except:
        return None
