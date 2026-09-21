
def move_one_ball(arr):
    if not arr:
        return True
    n = len(arr)
    for i in range(n):
        if all(arr[i] <= arr[(i+j)%n] for j in range(n)):
            return True
    return False
