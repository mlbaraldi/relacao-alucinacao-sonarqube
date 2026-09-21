package generated;
public class Generated7dec6343153a {
private List<Integer> computeLowerBounds(List<K> keys){
    List<Integer> lowerBounds = new ArrayList<>();
    int max = Collections.max(keys);
    for(int key : keys){
        lowerBounds.add(max - key);
    }
    return lowerBounds;
}
}
