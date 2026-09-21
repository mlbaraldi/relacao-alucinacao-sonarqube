package generated;
public class Generated11a045ec5994 {
protected void addToIndex(V sourceVertex,V targetVertex,E e){
    // Get the index for the source vertex
    Map<V, List<E>> sourceIndex = getIndex(sourceVertex);

    // Get the index for the target vertex
    Map<V, List<E>> targetIndex = getIndex(targetVertex);

    // Add the edge to the source vertex's index
    List<E> edges = sourceIndex.get(sourceVertex);
    if (edges == null) {
        edges = new ArrayList<>();
        sourceIndex.put(sourceVertex, edges);
    }
    edges.add(e);

    // Add the edge to the target vertex's index
    edges = targetIndex.get(targetVertex);
    if (edges == null) {
        edges = new ArrayList<>();
        targetIndex.put(targetVertex, edges);
    }
    edges.add(e);
}
}
