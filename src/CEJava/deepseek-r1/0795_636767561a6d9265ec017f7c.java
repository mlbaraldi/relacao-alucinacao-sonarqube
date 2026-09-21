package generated;
public class Generateda37ad8654843 {
protected GraphPath<V,E> edgeSetToTour(Set<E> tour,Graph<V,E> graph){
    if (tour.isEmpty()) {
        throw new IllegalArgumentException("Tour is empty");
    }

    List<E> edgeList = new ArrayList<>();
    Set<E> remainingEdges = new HashSet<>(tour);

    // Get the first edge to start the path
    E firstEdge = remainingEdges.iterator().next();
    remainingEdges.remove(firstEdge);
    edgeList.add(firstEdge);

    V startVertex = graph.getEdgeSource(firstEdge);
    V currentEnd = graph.getEdgeTarget(firstEdge);
    boolean isUndirected = graph.getType().isUndirected();

    while (!remainingEdges.isEmpty()) {
        E nextEdge = null;
        V nextEnd = null;

        // Find the next edge connected to currentEnd
        for (E edge : remainingEdges) {
            V source = graph.getEdgeSource(edge);
            V target = graph.getEdgeTarget(edge);

            if (isUndirected) {
                if (source.equals(currentEnd)) {
                    nextEdge = edge;
                    nextEnd = target;
                    break;
                } else if (target.equals(currentEnd)) {
                    nextEdge = edge;
                    nextEnd = source;
                    break;
                }
            } else {
                // Directed graph: next edge's source must be currentEnd
                if (source.equals(currentEnd)) {
                    nextEdge = edge;
                    nextEnd = target;
                    break;
                }
            }
        }

        if (nextEdge == null) {
            throw new IllegalArgumentException("Tour is disconnected");
        }

        edgeList.add(nextEdge);
        remainingEdges.remove(nextEdge);
        currentEnd = nextEnd;
    }

    // Verify that the tour forms a cycle
    if (!currentEnd.equals(startVertex)) {
        throw new IllegalArgumentException("Tour does not form a cycle");
    }

    // Calculate the total weight of the path
    double totalWeight = 0.0;
    for (E edge : edgeList) {
        totalWeight += graph.getEdgeWeight(edge);
    }

    return new GraphPathImpl<>(graph, startVertex, currentEnd, edgeList, totalWeight);
}
}
