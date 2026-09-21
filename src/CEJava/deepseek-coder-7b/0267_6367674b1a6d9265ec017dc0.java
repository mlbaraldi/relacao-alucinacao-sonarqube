package generated;
public class Generatedd50045c35487 {
private Set<V> initVisibleVertices(){
    Set<V> visibleVertices = new HashSet<>();
    for (Map.Entry<V, List<V>> entry : adjacencyList.entrySet()) {
        if (!entry.getValue().isEmpty()) {
            visibleVertices.add(entry.getKey());
        }
    }
    return visibleVertices;
}
}
