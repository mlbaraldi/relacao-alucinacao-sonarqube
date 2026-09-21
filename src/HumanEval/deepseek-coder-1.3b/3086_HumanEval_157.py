
def right_angle_triangle(a, b, c):
    # Check if any side is zero
    if a == 0 or b == 0 or c == 0:
        return False
    # Check if any side is equal to the sum of the other two
    elif a == b + c or b == a + c or c == a + b:
        return True
    else:
        return False
