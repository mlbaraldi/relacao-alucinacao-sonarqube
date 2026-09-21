

def dehydrate_point(value):
    """
    Dehydrator for Point data.

    :param value: Point object
    :type value: Point
    :return: Dictionary representation of the Point object
    :rtype: dict
    """
    return {
        'x': value.x,
        'y': value.y,
        'z': value.z
    }
