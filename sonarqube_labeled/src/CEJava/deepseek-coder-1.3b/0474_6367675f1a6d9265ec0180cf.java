package generated;
public class Generatede9ae6bcaba2a {
private static <V,E>boolean isClique(Graph<V,E> graph,Set<V> vertices){
    for (V vertex1 : vertices) {
        for (V vertex2 : vertices) {
            if (!graph.hasEdge(vertex1, vertex2)) {
                return false;
            }
        }
    }
    return true;
}
}
