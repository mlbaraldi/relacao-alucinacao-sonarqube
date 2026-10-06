
def add_elements(arr, k):
    sum = 0
    for i in range(k):
        if arr[i] >= 0 and arr[i] <= 99:
            sum += arr[i]
    return sum
