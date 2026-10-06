package generated;
public class Generated7dec6343153a {
private List<Integer> computeLowerBounds(List<K> keys){
    List<Integer> lowerBounds = new ArrayList<>();
    for (K key : keys) {
        int lowerBound = 0;
        for (int i = 0; i < keys.size(); i++) {
            if (keys.get(i).compareTo(key) > 0) {
                lowerBound++;
            }
        }
        lowerBounds.add(lowerBound);
    }
    return lowerBounds;
}
}
