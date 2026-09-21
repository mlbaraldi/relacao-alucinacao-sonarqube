package generated;
public class Generateda37ad8654843 {
protected GraphPath<V,E> edgeSetToTour(Set<E> tour,Graph<V,E> graph){
    List<V> vertices = new ArrayList<>();
    for (E edge : tour) {
        V source = graph.getEdgeSource(edge);
        V target = graph.getEdgeTarget(edge);
        vertices.add(source);
        vertices.add(target);
    }
    return new GraphPath<>(graph, vertices, 0, vertices.size() - 1);
}
}
