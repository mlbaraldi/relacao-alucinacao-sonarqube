
def intersection(interval1, interval2):
    """Determine if the length of the intersection of two intervals is a prime number."""
    # Find the intersection of the two intervals
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    # If the intervals don't intersect, return "NO"
    if start > end:
        return "NO"

    # Check if the length of the intersection is a prime number
    length = end - start + 1
    return "YES" if is_prime(length) else "NO"
