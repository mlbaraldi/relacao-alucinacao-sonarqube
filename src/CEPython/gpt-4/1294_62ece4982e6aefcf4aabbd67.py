

def vertex3tuple(vertices):
    # Create a list to store the 3-tuples
    tuples = []
    
    # Get the number of vertices
    num_vertices = len(vertices)
    
    # Loop over the vertices
    for i in range(num_vertices):
        # Get the vertex and the two vertices on either side
        prev_vertex = vertices[(i-1) % num_vertices]
        curr_vertex = vertices[i]
        next_vertex = vertices[(i+1) % num_vertices]
        
        # Add the 3-tuple to the list
        tuples.append((prev_vertex, curr_vertex, next_vertex))
    
    # Return the list of 3-tuples
    return tuples
