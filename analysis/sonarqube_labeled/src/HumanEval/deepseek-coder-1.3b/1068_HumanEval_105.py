
def by_length(arr):
    # Filter out the numbers between 1 and 9
    filtered_arr = [num for num in arr if 1 <= num <= 9]

    # Sort the numbers
    sorted_arr = sorted(filtered_arr)

    # Reverse the sorted array
    reversed_arr = sorted_arr[::-1]

    # Map the numbers to their names
    mapped_arr = [str(num) for num in reversed_arr]

    # Map the names to their corresponding numbers
    final_arr = [str(num) for num in mapped_arr]

    return final_arr
