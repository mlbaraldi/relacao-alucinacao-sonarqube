
def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    # Check if the array is already sorted
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            break
    else:
        return True
    # Count the number of drops
    count = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            count += 1
    # Check conditions for being a rotated sorted array
    return count == 1 and arr[-1] <= arr[0]
