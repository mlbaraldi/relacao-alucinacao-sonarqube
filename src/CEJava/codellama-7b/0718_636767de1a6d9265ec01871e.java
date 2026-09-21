package generated;
public class Generateda25609d4d0e6 {
private void check(String modelName) throws IllegalStateException {
    // Get the sharding key indices for the given model name
    List<Integer> shardingKeyIndices = getShardingKeyIndices(modelName);

    // Check if the sharding key indices are continuous
    if (!isContinuous(shardingKeyIndices)) {
        throw new IllegalStateException("Sharding key indices are not continuous for model " + modelName);
    }
}
}
