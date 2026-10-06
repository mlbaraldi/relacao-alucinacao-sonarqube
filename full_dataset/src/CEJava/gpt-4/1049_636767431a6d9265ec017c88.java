package generated;
public class Generated7dec6343153a {
private List<Integer> computeLowerBounds(List<K> keys){
    List<Integer> lowerBounds = new ArrayList<>();
    for (Integer key : keys) {
        lowerBounds.add(key - 1);
    }
    return lowerBounds;
}
}
