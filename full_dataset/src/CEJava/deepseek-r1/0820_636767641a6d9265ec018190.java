package generated;
public class Generated22431d4e3098 {
private void reload(List<Set<Integer>> bucketsByLabel,List<Integer> labels,int minLabel){
    Set<Integer> minBucket = bucketsByLabel.get(minLabel);
    Set<Integer> zeroBucket = bucketsByLabel.get(0);
    for (Integer v : minBucket) {
        labels.set(v, 0);
        zeroBucket.add(v);
    }
    minBucket.clear();
}
}
