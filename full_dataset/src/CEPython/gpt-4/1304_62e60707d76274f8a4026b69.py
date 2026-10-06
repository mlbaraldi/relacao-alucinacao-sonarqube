from collections import namedtuple


def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.
    """
    # Create a namedtuple subclass with the given name and fields
    Point = namedtuple(name, fields)

    # Add a new method to the class to get the SRID
    def get_srid(self):
        return srid_map[self.__class__.__name__]

    # Add the new method to the class
    Point.get_srid = get_srid

    # Return the new class
    return Point
