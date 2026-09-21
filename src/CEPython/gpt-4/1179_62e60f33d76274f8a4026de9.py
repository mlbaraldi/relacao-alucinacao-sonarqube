

def dehydrate_point(value):
    """
    Dehydrator for Point data.

    :param value: Point object
    :type value: Point
    :return: Dictionary with x and y coordinates of the point
    :rtype: dict
    """
    return {'x': value.x, 'y': value.y}
