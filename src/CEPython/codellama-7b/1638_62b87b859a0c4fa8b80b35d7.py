

def to_csv(self, separator=",", header=None):
    """
    Convert graph's points to CSV.

    *separator* delimits values, the default is comma.

    *header*, if not ``None``, is the first string of the output
    (new line is added automatically).

    Since a graph can be multidimensional,
    for each point first its coordinate is converted to string
    (separated by *separator*), then each part of its value.

    To convert :class:`Graph` to CSV inside a Lena sequence,
    use :class:`lena.output.ToCSV`.
    """
    # Check if the graph is multidimensional
    if len(self.points) > 1:
        # If the graph is multidimensional, convert each point to a string
        # using the separator
        points_str = [separator.join(map(str, point)) for point in self.points]
    else:
        # If the graph is unidimensional, convert each point to a string
        # using the separator
        points_str = [separator.join(map(str, point)) for point in self.points[0]]

    # If a header is provided, add it to the beginning of the output
    if header is not None:
        points_str = [header] + points_str

    # Return the output as a string
    return "\n".join(points_str)
