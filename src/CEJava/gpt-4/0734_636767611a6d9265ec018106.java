package generated;
public class Generated9af99103ebc8 {
public double vertexWeight(Set<V> v){
    double sum = 0;
    for (Edge edge : getEdges()) {
        if (edge.getDestination().equals(v)) {
            sum += edge.getWeight();
        }
    }
    return sum;
}
}
