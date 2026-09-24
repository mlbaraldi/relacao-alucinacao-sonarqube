
def intersection(interval1, interval2):
    # Find the intersection of the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # If there is no intersection, return "NO"
    if start > end:
        return "NO"

    # If the intersection is a prime number, return "YES", otherwise "NO"
    if end - start + 1 in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        return "YES"
    else:
        return "NO"
