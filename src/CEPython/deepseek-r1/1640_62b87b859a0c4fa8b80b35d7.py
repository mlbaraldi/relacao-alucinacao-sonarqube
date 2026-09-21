def to_csv(self, separator=",", header=None):
    """
    Convert graph's points to CSV.

    :param separator: Delimiter for values, defaults to ",".
    :param header: Optional header string added as the first line.
    :return: CSV formatted string.
    """
    lines = []
    if header is not None:
        lines.append(header)
    for coord, val in self.points:
        # Process coordinate
        if isinstance(coord, (list, tuple)):
            coord_parts = list(map(str, coord))
        else:
            coord_parts = [str(coord)]
        # Process value
        if isinstance(val, (list, tuple)):
            val_parts = list(map(str, val))
        else:
            val_parts = [str(val)]
        # Combine parts and add to lines
        line = separator.join(coord_parts + val_parts)
        lines.append(line)
    return '\n'.join(lines)
