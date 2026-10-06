
def intersection(interval1, interval2):
    a1, b1 = interval1
    a2, b2 = interval2
    start = max(a1, a2)
    end = min(b1, b2)
    if start > end:
        return "NO"
    length = end - start
    if length < 2:
        return "NO"
    if length == 2:
        return "YES"
    if length % 2 == 0:
        return "NO"
    for i in range(3, int(length ** 0.5) + 1, 2):
        if length % i == 0:
            return "NO"
    return "YES"
