package generated;
public class Generateda25609d4d0e6 {
private void check(String modelName) throws IllegalStateException {
    List<Integer> indices = getShardingKeyIndices(modelName);
    Collections.sort(indices);
    for (int i = 0; i < indices.size() - 1; i++) {
        if (indices.get(i) + 1 != indices.get(i + 1)) {
            throw new IllegalStateException("Sharding key indices are not continuous for model: " + modelName);
        }
    }
}
}
