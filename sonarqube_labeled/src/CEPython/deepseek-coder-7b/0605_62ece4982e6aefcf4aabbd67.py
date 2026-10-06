

def vertex3tuple(vertices):
    """
    return 3 points for each vertex of the polygon. This will include the vertex and the 2 points on both sides of the vertex::

    polygon with vertices ABCD
    Will return
    DAB, ABC, BCD, CDA -> returns 3tuples
    #A    B    C    D  -> of vertices
    """
    vertices = list(vertices)  # Ensure vertices is a list
    n = len(vertices)
    tuples = []

    for i in range(n):
        # Get the next and previous vertices
        next_vertex = vertices[(i + 1) % n]
        prev_vertex = vertices[(i - 1) % n]

        # Create the 3-tuple
        tuples.append((vertices[i], next_vertex, prev_vertex))

    return tuples
