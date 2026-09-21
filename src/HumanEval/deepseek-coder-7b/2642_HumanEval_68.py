
def pluck(arr):
    # Initialize variables to store the smallest even number and its index
    smallest_even = float('inf')
    smallest_index = -1

    # Iterate over the array
    for i, num in enumerate(arr):
        # Check if the number is even and smaller than the current smallest even number
        if num % 2 == 0 and num <= smallest_even:
            # Update the smallest even number and its index
            smallest_even = num
            smallest_index = i

    # If a smallest even number was found, return it in the required format
    if smallest_even != float('inf'):
        return [smallest_even, smallest_index]

    # If no smallest even number was found, return an empty list
    return []
