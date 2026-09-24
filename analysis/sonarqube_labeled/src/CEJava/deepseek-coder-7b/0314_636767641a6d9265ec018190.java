package generated;
public class Generated22431d4e3098 {
private void reload(List<Set<Integer>> bucketsByLabel,List<Integer> labels,int minLabel){
    // Find the bucket with label minLabel
    Set<Integer> minLabelBucket = bucketsByLabel.get(minLabel);

    // If the bucket is not empty
    if (!minLabelBucket.isEmpty()) {
        // Create a new bucket with label 0 if it doesn't exist
        if (bucketsByLabel.get(0) == null) {
            bucketsByLabel.set(0, new HashSet<>());
        }

        // Move all vertices from the minLabel bucket to the bucket with label 0
        bucketsByLabel.get(0).addAll(minLabelBucket);

        // Clear the minLabel bucket
        minLabelBucket.clear();

        // Update the labeling
        for (int i = 0; i < labels.size(); i++) {
            if (labels.get(i) == minLabel) {
                labels.set(i, 0);
            }
        }
    }
}
}
