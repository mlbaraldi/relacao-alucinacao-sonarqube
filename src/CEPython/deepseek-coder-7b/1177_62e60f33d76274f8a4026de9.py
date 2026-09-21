

def dehydrate_point(value):
    """
    Dehydrator for Point data.

    :param value: Point object
    :type value: Point
    :return: dictionary with x and y coordinates
    """
    if isinstance(value, Point):
        return {'x': value.x, 'y': value.y}
    else:
        raise ValueError("The provided value is not a Point object")
