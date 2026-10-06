

def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.
    """
    # Create the class
    Point = type(name, (object,), {})

    # Add fields to the class
    for field in fields:
        setattr(Point, field, None)

    # Add SRID mapping to the class
    for field, srid in srid_map.items():
        setattr(Point, field, srid)

    return Point
