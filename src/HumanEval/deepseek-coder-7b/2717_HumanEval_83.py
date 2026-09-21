
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # The count of n-digit numbers that start or end with 1
    count = 0

    # The first n-digit number that starts or ends with 1
    start = 10**(n-1)

    # The last n-digit number that starts or ends with 1
    end = 10**n - 1

    # Count the numbers that start or end with 1
    for i in range(start, end+1):
        if i % 10 == 1 or i // 10**(n-1) == 1:
            count += 1

    return count
