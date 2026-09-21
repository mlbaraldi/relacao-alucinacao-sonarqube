package generated;
public class Generated9af99103ebc8 {
public double vertexWeight(Set<V> v){
    double total = 0.0;
    for (V vertex : v) {
        for (Edge<V> edge : getIncomingEdges(vertex)) {
            total += edge.getWeight();
        }
    }
    return total;
}
}
