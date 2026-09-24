package generated;
public class Generated99153d3f66c2 {
@Override public boolean hasNext(){
    for (Vertex vertex : vertices) {
        if (!vertex.visited) {
            return true;
        }
    }
    return false;
}
}
