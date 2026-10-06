
def sort_array(array):
    # If the array is empty, return it
    if not array:
        return array

    # Calculate the sum of the first and last element of the array
    sum_first_last = array[0] + array[-1]

    # If the sum is odd, sort the array in ascending order
    if sum_first_last % 2 != 0:
        return sorted(array)

    # If the sum is even, sort the array in descending order
    else:
        return sorted(array, reverse=True)
