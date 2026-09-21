package generated;
public class Generated34f2343f90c2 {
public static <V,E>IsomorphicGraphMapping<V,E> identity(Graph<V,E> graph){
    Map<V, V> forwardMap = new HashMap<>();
    for (V v : graph.vertexSet()) {
        forwardMap.put(v, v);
    }
    return new IsomorphicGraphMapping<>(forwardMap, forwardMap, graph, graph);
}
}
