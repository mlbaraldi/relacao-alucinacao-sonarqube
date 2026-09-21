package generated;
public class Generatedd50045c35487 {
private Set<V> initVisibleVertices(){
    Set<V> visibleVertices = new HashSet<>();
    for (E edge : edges) {
        V vertex = edge.getVertex();
        if (vertex.getDegree() > 0) {
            visibleVertices.add(vertex);
        }
    }
    return visibleVertices;
}
}
