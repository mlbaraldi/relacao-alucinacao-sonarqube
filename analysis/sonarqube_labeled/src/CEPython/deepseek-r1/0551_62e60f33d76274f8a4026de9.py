def dehydrate_point(value):
    """
    Dehydrator for Point data.

    :param value: Point object to dehydrate
    :type value: Point
    :return: Dictionary representing the Point in GeoJSON format
    :rtype: dict
    """
    return {
        'type': 'Point',
        'coordinates': [value.x, value.y]
    }
