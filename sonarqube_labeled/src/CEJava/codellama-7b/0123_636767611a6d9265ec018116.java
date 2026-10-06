package generated;
public class Generatedcda9a29c2f21 {
private Set<V> intersection(Set<V> set1,Set<V> set2){
    Set<V> intersection = new HashSet<>();
    for (V element : set1) {
        if (set2.contains(element)) {
            intersection.add(element);
        }
    }
    return intersection;
}
}
