
def can_arrange(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            for j in range(i-1, -1, -1):
                if arr[j] < arr[i]:
                    return i
    return -1
