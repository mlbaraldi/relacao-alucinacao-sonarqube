package generated;
public class Generatedcda9a29c2f21 {
private Set<V> intersection(Set<V> set1,Set<V> set2){
    Set<V> intersection = new HashSet<>(set1);
    intersection.retainAll(set2);
    return intersection;
}
}
