
def iscube(a):
    '''
    Determines if the integer a is a cube of some integer.
    '''
    if a == 0:
        return True
    abs_a = abs(a)
    low = 0
    high = abs_a
    while low <= high:
        mid = (low + high) // 2
        cube = mid ** 3
        if cube == abs_a:
            return True
        elif cube < abs_a:
            low = mid + 1
        else:
            high = mid - 1
    return False
