package generated;
public class Generatedd50045c35487 {
private Set<V> initVisibleVertices(){
    Set<V> visibleVertices = new HashSet<>();

    for (Edge e : edges) {
        V vertex1 = e.getVertex1();
        V vertex2 = e.getVertex2();

        if (vertex1.getDegree() > 0) {
            visibleVertices.add(vertex1);
        }

        if (vertex2.getDegree() > 0) {
            visibleVertices.add(vertex2);
        }
    }

    return visibleVertices;
}
}
