package generated;
public class Generatedd50045c35487 {
private Set<V> initVisibleVertices(){
    Set<V> visibleVertices = new HashSet<>();
    for (Edge<V> edge : getEdges()) {
        visibleVertices.add(edge.getSource());
        visibleVertices.add(edge.getTarget());
    }
    return visibleVertices;
}
}
