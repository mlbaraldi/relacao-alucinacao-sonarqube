package generated;
public class Generated22431d4e3098 {
private void reload(List<Set<Integer>> bucketsByLabel,List<Integer> labels,int minLabel){
    // Check if minLabel is valid
    if (minLabel < 0 || minLabel >= bucketsByLabel.size()) {
        throw new IllegalArgumentException("Invalid minLabel");
    }

    // Get the bucket with minLabel
    Set<Integer> minBucket = bucketsByLabel.get(minLabel);

    // Move all vertices from minBucket to bucket 0
    bucketsByLabel.get(0).addAll(minBucket);

    // Update the labels of the moved vertices
    for (Integer vertex : minBucket) {
        labels.set(vertex, 0);
    }

    // Clear the minBucket
    minBucket.clear();
}
}
