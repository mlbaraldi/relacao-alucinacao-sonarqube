package generated;
public class Generated9af99103ebc8 {
public double vertexWeight(Set<V> v){
    double sum = 0;
    for (Vertex vertex : vertices) {
        sum += vertex.getWeight();
    }
    return sum;
}
}
