
def search(lst):
    # Check if the list is empty
    if not lst:
        return -1

    # Sort the list in descending order
    lst.sort(reverse=True)

    # Initialize the greatest integer with the first element
    greatest = lst[0]

    # Iterate over the list and find the first integer with a frequency greater than or equal to itself
    for i in range(1, len(lst)):
        if lst[i] >= greatest and lst.count(lst[i]) >= lst[i]:
            greatest = lst[i]
            break

    # Return the greatest integer if it exists, otherwise return -1
    return greatest if greatest > 0 else -1
