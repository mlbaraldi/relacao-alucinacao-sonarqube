package generated;
public class Generateda25609d4d0e6 {
private void check(String modelName) throws IllegalStateException {
    List<Integer> indices = getShardingKeyIndices(modelName);
    if (indices.size() <= 1) {
        return;
    }
    List<Integer> sortedIndices = new ArrayList<>(indices);
    Collections.sort(sortedIndices);
    for (int i = 1; i < sortedIndices.size(); i++) {
        if (sortedIndices.get(i) - sortedIndices.get(i - 1) != 1) {
            throw new IllegalStateException("Sharding key indices are not continuous for model " + modelName);
        }
    }
}
}
