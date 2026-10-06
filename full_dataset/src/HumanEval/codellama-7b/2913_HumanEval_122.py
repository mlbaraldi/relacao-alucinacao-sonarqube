
def add_elements(arr, k):
    # Check if the input is valid
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid input")

    # Initialize the sum to 0
    sum = 0

    # Iterate over the first k elements of the array
    for i in range(k):
        # Check if the current element has at most two digits
        if len(str(arr[i])) <= 2:
            # Add the current element to the sum
            sum += arr[i]

    # Return the sum
    return sum
