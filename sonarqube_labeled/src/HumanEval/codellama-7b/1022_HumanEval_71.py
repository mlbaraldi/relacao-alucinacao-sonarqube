
def triangle_area(a, b, c):
    if a + b < c or b + c < a or c + a < b:
        return -1
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return round(area, 2)
