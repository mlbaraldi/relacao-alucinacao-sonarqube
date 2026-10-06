

def to_csv(self, separator=",", header=None):
    csv_lines = []
    if header:
        csv_lines.append(header)
    for point in self.points:
        csv_lines.append(separator.join(str(coord) for coord in point))
    return "\n".join(csv_lines)
