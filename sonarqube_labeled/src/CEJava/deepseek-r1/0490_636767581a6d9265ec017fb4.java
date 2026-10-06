package generated;
public class Generateda2104ac3f2af {
private List<Integer> computeUpperBounds(List<K> keys){
    List<Integer> upperBounds = new ArrayList<>();
    for (K key : keys) {
        K minUpper = null;
        for (K candidate : keys) {
            if (candidate.compareTo(key) > 0) {
                if (minUpper == null || candidate.compareTo(minUpper) < 0) {
                    minUpper = candidate;
                }
            }
        }
        if (minUpper == null) {
            upperBounds.add((Integer) key);
        } else {
            upperBounds.add((Integer) minUpper);
        }
    }
    return upperBounds;
}
}
