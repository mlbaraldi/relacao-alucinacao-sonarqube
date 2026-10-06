

def vertex3tuple(vertices):
    result = []
    for i in range(len(vertices)):
        vertex = vertices[i]
        left = vertices[(i - 1) % len(vertices)]
        right = vertices[(i + 1) % len(vertices)]
        result.append((vertex, left, right))
    return result
