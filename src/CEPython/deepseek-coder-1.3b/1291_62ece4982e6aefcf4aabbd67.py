

def vertex3tuple(vertices):
    """
    Return 3 points for each vertex of the polygon. This will include the vertex and the 2 points on both sides of the vertex.

    Parameters:
    vertices (list): A list of vertices in the form of (x, y) tuples.

    Returns:
    list: A list of tuples, where each tuple contains 3 points.
    """
    result = []
    for vertex in vertices:
        x, y = vertex
        result.append((x, y, x))
        result.append((x, y, -x))
        result.append((-x, y, x))
        result.append((-x, y, -x))
    return result
