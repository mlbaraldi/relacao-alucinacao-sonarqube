package generated;
public class Generated22431d4e3098 {
private void reload(List<Set<Integer>> bucketsByLabel,List<Integer> labels,int minLabel){
    // Move all vertices from the bucket with label minLabel to the bucket with label 0
    for (int i = 0; i < bucketsByLabel.size(); i++) {
        if (i == minLabel) {
            bucketsByLabel.get(i).forEach(vertex -> {
                bucketsByLabel.get(0).add(vertex);
                labels.set(vertex, 0);
            });
        }
    }

    // Clear the bucket with label minLabel
    bucketsByLabel.get(minLabel).clear();

    // Update the labeling accordingly
    for (int i = 0; i < labels.size(); i++) {
        if (labels.get(i) == minLabel) {
            labels.set(i, 0);
        }
    }
}
}
