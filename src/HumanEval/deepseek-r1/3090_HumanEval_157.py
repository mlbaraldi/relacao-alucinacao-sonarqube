
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    '''
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    sorted_sides = sorted([a, b, c])
    
    if sorted_sides[0] + sorted_sides[1] <= sorted_sides[2]:
        return False
    
    return (sorted_sides[0] ** 2 + sorted_sides[1] ** 2) == (sorted_sides[2] ** 2)
