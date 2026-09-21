
def smallest_change(arr):
    # Initialize variables to keep track of the minimum number of changes and the current palindrome
    min_changes = float('inf')
    current_palindrome = []

    # Iterate through the array and check if the current element is already in the palindrome
    for i in range(len(arr)):
        if arr[i] in current_palindrome:
            continue

        # If the current element is not in the palindrome, add it to the palindrome and update the minimum number of changes
        current_palindrome.append(arr[i])
        min_changes = min(min_changes, len(current_palindrome))

    # If the array is already palindromic, return 0
    if len(current_palindrome) == len(arr):
        return 0

    # Return the minimum number of changes
    return min_changes
