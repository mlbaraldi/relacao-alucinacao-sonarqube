package generated;
public class Generated34f2343f90c2 {
public static <V,E>IsomorphicGraphMapping<V,E> identity(Graph<V,E> graph){
    IsomorphicGraphMapping<V,E> mapping = new IsomorphicGraphMapping<>();
    mapping.setSourceGraph(graph);
    mapping.setTargetGraph(graph);
    mapping.setIsIsomorphic(true);
    return mapping;
}
}
