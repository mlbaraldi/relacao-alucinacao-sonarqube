package generated;
public class Generated11a045ec5994 {
protected void addToIndex(V sourceVertex,V targetVertex,E e){
    // Assuming edges is a Map of Maps to store the edges
    Map<V, Map<V, E>> edges;

    // Check if the source vertex is already in the index
    if (!edges.containsKey(sourceVertex)) {
        // If not, add a new entry for the source vertex
        edges.put(sourceVertex, new HashMap<>());
    }

    // Add the edge to the index
    edges.get(sourceVertex).put(targetVertex, e);
}
}
