package generated;
public class Generated9af99103ebc8 {
public double vertexWeight(Set<V> v){
    double weightSum = 0.0;
    for (Edge e : g.getEdges()) {
        if (e.getEndVertex().equals(v)) {
            weightSum += e.getWeight();
        }
    }
    return weightSum;
}
}
