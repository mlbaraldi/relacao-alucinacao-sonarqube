def point_type(name, fields, srid_map):
    """
    Dynamically create a Point subclass.
    """
    def __init__(self, srid, **kwargs):
        if srid not in srid_map:
            raise ValueError(f"SRID {srid} is not supported.")
        required_fields = srid_map[srid]
        missing = [field for field in required_fields if field not in kwargs]
        if missing:
            raise ValueError(f"Missing required fields for SRID {srid}: {', '.join(missing)}")
        extra = [field for field in kwargs if field not in required_fields]
        if extra:
            raise ValueError(f"Unexpected fields for SRID {srid}: {', '.join(extra)}")
        for field in required_fields:
            setattr(self, field, kwargs[field])
    
    cls = type(name, (Point,), {
        '__init__': __init__,
        '_fields': fields,
        '_srid_map': srid_map
    })
    return cls
