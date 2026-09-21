
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, col in enumerate(row):
            if col == x:
                result.append((i, j))
    return sorted(result, key=lambda t: (t[0], -t[1]))
