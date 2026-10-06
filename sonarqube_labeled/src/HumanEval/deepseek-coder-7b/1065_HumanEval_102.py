
def choose_num(x, y):
    # Ensure x is the smaller number
    if x > y:
        x, y = y, x

    # Start from the larger number and go down to the smaller number
    for i in range(y, x-1, -1):
        # Check if the number is even
        if i % 2 == 0:
            return i

    # If no even number is found, return -1
    return -1
