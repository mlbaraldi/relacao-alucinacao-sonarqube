
def triangle_area(a, b, c):
    # Check if the sides form a valid triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return -1

    # Calculate the semi-perimeter
    s = (a + b + c) / 2

    # Calculate the area using Heron's formula
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

    # Round the area to 2 decimal points and return
    return round(area, 2)
