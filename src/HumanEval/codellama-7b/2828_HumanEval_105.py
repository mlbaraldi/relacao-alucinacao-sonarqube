
def by_length(arr):
    # Check if the array is empty
    if not arr:
        return []

    # Sort the array
    arr.sort()

    # Reverse the array
    arr.reverse()

    # Replace each digit by its corresponding name
    names = []
    for num in arr:
        if num >= 1 and num <= 9:
            names.append(str(num) + " " + str(num))
        else:
            names.append(str(num))

    return names
