

def to_csv(self, separator=",", header=None):
    result = []
    if header is not None:
        result.append(header)
    for point in self.points:
        coordinates, values = point
        coordinates_str = separator.join(map(str, coordinates))
        values_str = separator.join(map(str, values))
        result.append(coordinates_str + separator + values_str)
    return "\n".join(result)
