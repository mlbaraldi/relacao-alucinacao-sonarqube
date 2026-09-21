
def add_elements(arr, k):
    # Initialize the sum to 0
    sum = 0

    # Iterate over the first k elements of the array
    for i in range(k):
        # Check if the current element has at most two digits
        if arr[i] >= -99 and arr[i] <= 99:
            # Add the current element to the sum
            sum += arr[i]

    # Return the sum
    return sum
