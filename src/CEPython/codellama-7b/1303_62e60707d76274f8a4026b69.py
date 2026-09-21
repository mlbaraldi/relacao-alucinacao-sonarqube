

def point_type(name, fields, srid_map):
    class Point(object):
        def __init__(self, *args, **kwargs):
            self.name = name
            self.fields = fields
            self.srid_map = srid_map
            for field in fields:
                setattr(self, field, None)

        def __str__(self):
            return f"{self.name}({', '.join(self.fields)})"

        def __repr__(self):
            return f"{self.name}({', '.join(self.fields)})"

        def __eq__(self, other):
            return self.name == other.name and self.fields == other.fields

        def __ne__(self, other):
            return not self.__eq__(other)

        def __hash__(self):
            return hash(self.name)

        def __getitem__(self, key):
            return getattr(self, key)

        def __setitem__(self, key, value):
            setattr(self, key, value)

        def __delitem__(self, key):
            delattr(self, key)

        def __contains__(self, key):
            return hasattr(self, key)

        def __iter__(self):
            return iter(self.fields)

        def __len__(self):
            return len(self.fields)

        def __add__(self, other):
            return Point(self.name, self.fields + other.fields, self.srid_map)

        def __radd__(self, other):
            return Point(self.name, self.fields + other.fields, self.srid_map)

        def __sub__(self, other):
            return Point(self.name, self.fields - other.fields, self.srid_map)

        def __rsub__(self, other):
            return Point(self.name, other.fields - self.fields, self.srid_map)
