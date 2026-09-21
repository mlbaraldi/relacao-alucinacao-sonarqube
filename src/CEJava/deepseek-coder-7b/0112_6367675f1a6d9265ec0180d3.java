package generated;
public class Generated34f2343f90c2 {
public static <V,E>IsomorphicGraphMapping<V,E> identity(Graph<V,E> graph){
    IsomorphicGraphMapping<V, E> mapping = new IsomorphicGraphMapping<>();
    for (V vertex : graph.vertexToEdgeMap.keySet()) {
        mapping.addMapping(vertex, vertex);
    }
    return mapping;
}
}
