package generated;
public class Generateda37ad8654843 {
protected GraphPath<V,E> edgeSetToTour(Set<E> tour,Graph<V,E> graph){
    // Create a list to store the vertices in the order they are visited
    List<V> vertexList = new ArrayList<>();

    // Choose an arbitrary edge to start
    E startEdge = tour.iterator().next();
    V currentVertex = graph.getEdgeSource(startEdge);
    V startVertex = currentVertex;
    vertexList.add(currentVertex);

    // Remove the starting edge from the tour set
    tour.remove(startEdge);

    // While there are still edges in the tour
    while (!tour.isEmpty()) {
        // Find the next edge in the tour that is connected to the current vertex
        for (Iterator<E> iterator = tour.iterator(); iterator.hasNext();) {
            E edge = iterator.next();
            if (graph.getEdgeSource(edge).equals(currentVertex) || graph.getEdgeTarget(edge).equals(currentVertex)) {
                // Add the other vertex of the edge to the vertex list
                currentVertex = graph.getEdgeSource(edge).equals(currentVertex) ? graph.getEdgeTarget(edge) : graph.getEdgeSource(edge);
                vertexList.add(currentVertex);

                // Remove the edge from the tour set
                iterator.remove();
                break;
            }
        }
    }

    // Add the start vertex to close the tour
    vertexList.add(startVertex);

    // Create a GraphPath object from the vertex list
    double tourWeight = HamiltonianCycleAlgorithmBase.calculateTourWeight(graph, vertexList);
    return new GraphWalk<>(graph, startVertex, startVertex, vertexList, tourWeight);
}
}
