package generated;
public class Generatede9ae6bcaba2a {
private static <V,E>boolean isClique(Graph<V,E> graph,Set<V> vertices){
    // Check if the given vertices form a complete subgraph
    Set<V> completeSubgraph = new HashSet<>(vertices);
    for (V vertex : vertices) {
        for (V neighbor : graph.getNeighbors(vertex)) {
            if (!completeSubgraph.contains(neighbor)) {
                return false;
            }
        }
    }
    return true;
}
}
