package generated;
public class Generatede9ae6bcaba2a {
private static <V,E>boolean isClique(Graph<V,E> graph,Set<V> vertices){
    // For each pair of vertices
    for (V v1 : vertices) {
        for (V v2 : vertices) {
            // Skip if it's the same vertex
            if (!v1.equals(v2)) {
                // If there is no edge between v1 and v2, then it's not a clique
                if (!graph.containsEdge(v1, v2)) {
                    return false;
                }
            }
        }
    }
    // If we haven't returned false by now, then it's a clique
    return true;
}
}
