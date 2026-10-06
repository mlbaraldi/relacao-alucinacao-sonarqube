package generated;
public class Generated22431d4e3098 {
private void reload(List<Set<Integer>> bucketsByLabel,List<Integer> labels,int minLabel){
    // Find the bucket with the minimum non-empty label
    int minNonEmptyLabel = -1;
    for (int i = 0; i < bucketsByLabel.size(); i++) {
        if (!bucketsByLabel.get(i).isEmpty()) {
            minNonEmptyLabel = i;
            break;
        }
    }

    // If there is a bucket with a non-empty label, move all vertices from that bucket to bucket 0
    if (minNonEmptyLabel != -1) {
        Set<Integer> bucket0 = bucketsByLabel.get(0);
        for (Integer vertex : bucketsByLabel.get(minNonEmptyLabel)) {
            bucket0.add(vertex);
        }
        bucketsByLabel.remove(minNonEmptyLabel);
        bucketsByLabel.add(0, bucket0);
    }

    // Update the labels
    for (int i = 0; i < labels.size(); i++) {
        if (labels.get(i) == minLabel) {
            labels.set(i, 0);
        }
    }
}
}
