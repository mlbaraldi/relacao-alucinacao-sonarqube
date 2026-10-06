package generated;
public class Generateda37ad8654843 {
protected GraphPath<V,E> edgeSetToTour(Set<E> tour,Graph<V,E> graph){
    // Create a new GraphPath
    GraphPath<V,E> graphPath = new GraphPath<>();

    // Add the first vertex of the tour to the path
    graphPath.addVertex(graph.getVertex(tour.iterator().next().getStartVertexId()));

    // Add the rest of the vertices in the tour to the path
    while (tour.iterator().hasNext()) {
        E edge = tour.iterator().next();
        graphPath.addVertex(graph.getVertex(edge.getEndVertexId()));
    }

    // Add the last vertex of the tour to the path
    graphPath.addVertex(graph.getVertex(tour.iterator().next().getEndVertexId()));

    return graphPath;
}
}
