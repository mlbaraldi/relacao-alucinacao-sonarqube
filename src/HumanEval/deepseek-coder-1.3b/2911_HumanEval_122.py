
def add_elements(arr, k):
    # Filter the first k elements of arr to only include numbers with at most two digits
    filtered_arr = [num for num in arr[:k] if all(int(digit) <= 2 for digit in str(num))]
    
    # Return the sum of the filtered numbers
    return sum(filtered_arr)
