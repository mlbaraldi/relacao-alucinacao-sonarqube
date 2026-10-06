package generated;
public class Generateda2104ac3f2af {
private List<Integer> computeUpperBounds(List<K> keys){
    List<Integer> upperBounds = new ArrayList<>();
    for (K key : keys) {
        int upperBound = 0;
        for (int i = 0; i < keys.size(); i++) {
            if (keys.get(i).compareTo(key) > 0) {
                upperBound = Math.max(upperBound, i);
            }
        }
        upperBounds.add(upperBound);
    }
    return upperBounds;
}
}
