
def move_one_ball(arr):
    if not arr:
        return True
    
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Check if the array is sorted in non-decreasing order
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True
