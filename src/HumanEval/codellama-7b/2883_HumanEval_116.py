
def sort_array(arr):
    # Convert the array to a list of tuples, where each tuple contains the
    # element and its binary representation
    binary_repr = [(element, bin(element)) for element in arr]

    # Sort the list of tuples based on the number of ones in the binary
    # representation, and then on the decimal value
    sorted_repr = sorted(binary_repr, key=lambda x: (x[1].count('1'), x[0]))

    # Return the sorted array
    return [element for element, _ in sorted_repr]
