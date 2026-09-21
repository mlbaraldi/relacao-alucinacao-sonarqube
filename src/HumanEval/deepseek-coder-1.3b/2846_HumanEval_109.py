
def move_one_ball(arr):
    if len(arr) == 0:
        return True
    else:
        for i in range(len(arr)):
            if arr[i:] + arr[:i] == sorted(arr[i:] + arr[:i]):
                return True
        return False
