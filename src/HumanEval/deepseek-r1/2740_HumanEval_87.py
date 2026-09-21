
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        columns = []
        for j, value in enumerate(row):
            if value == x:
                columns.append(j)
        columns.sort(reverse=True)
        for j in columns:
            result.append((i, j))
    return result
