
def tri(n):
    """Return the first n + 1 numbers of the Tribonacci sequence as defined."""
    if n == 0:
        return [1]
    res = [1, 3]
    if n == 1:
        return res
    for i in range(2, n + 1):
        if i % 2 == 0:
            res.append(1 + i // 2)
        else:
            term = res[i - 1] + res[i - 2] + 1 + (i + 1) // 2
            res.append(term)
    return res
