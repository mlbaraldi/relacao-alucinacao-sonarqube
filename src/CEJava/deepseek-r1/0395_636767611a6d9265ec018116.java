package generated;
public class Generatedcda9a29c2f21 {
private Set<V> intersection(Set<V> set1,Set<V> set2){
    Set<V> result = new HashSet<>();
    if (set1 == set2) {
        result.addAll(set1);
        return result;
    }
    if (set1.size() <= set2.size()) {
        for (V element : set1) {
            if (set2.contains(element)) {
                result.add(element);
            }
        }
    } else {
        for (V element : set2) {
            if (set1.contains(element)) {
                result.add(element);
            }
        }
    }
    return result;
}
}
