package generated;
public class Generated9af99103ebc8 {
public double vertexWeight(Set<V> v){
    double sum = 0;
    for (V neighbor : v) {
        sum += neighbor.getWeight();
    }
    return sum;
}
}
