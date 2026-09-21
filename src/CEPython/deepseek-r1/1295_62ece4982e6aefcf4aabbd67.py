def vertex3tuple(vertices):
    n = len(vertices)
    return [
        (vertices[(i-1) % n], vertices[i], vertices[(i+1) % n])
        for i in range(n)
    ]
