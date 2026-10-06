
def add(lst):
    # Check if the list is empty
    if not lst:
        raise ValueError("List is empty")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the list and add the even elements at odd indices
    for i in range(len(lst)):
        if i % 2 == 0:
            sum += lst[i]

    return sum
