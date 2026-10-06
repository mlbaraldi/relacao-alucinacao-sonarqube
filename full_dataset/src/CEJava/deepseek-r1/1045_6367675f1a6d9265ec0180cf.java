package generated;
public class Generatede9ae6bcaba2a {
private static <V,E>boolean isClique(Graph<V,E> graph,Set<V> vertices){
    List<V> vertexList = new ArrayList<>(vertices);
    for (int i = 0; i < vertexList.size(); i++) {
        V u = vertexList.get(i);
        for (int j = i + 1; j < vertexList.size(); j++) {
            V v = vertexList.get(j);
            if (!graph.containsEdge(u, v) && !graph.containsEdge(v, u)) {
                return false;
            }
        }
    }
    return true;
}
}
