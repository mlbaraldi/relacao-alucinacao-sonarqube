import attr


def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass with specified fields and SRID map.
    """
    # Create a class with the given name using attrs.define
    Point = attr.define(
        name,
        # Define attributes for the class
        attrs=(
            # Iterate over the fields and create attributes dynamically
            *(attr.ib(name=field) for field in fields)
        ),
        # Set the default class docstring
        doc="""A Point with dynamically defined attributes."""
    )
    
    # Set the SRID map as an attribute of the class
    Point.srid_map = srid_map
    
    return Point

# Example usage:
