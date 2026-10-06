package generated;
public class Generated71b03dbc71b6 {
@Override public void accept(final METRICS data){
    // Get the existing value from the cache
    METRICS existingValue = cache.get(data.getKey());

    // If the existing value is null, add the incoming data to the cache
    if (existingValue == null) {
        cache.put(data.getKey(), data);
    } else {
        // Merge the incoming data with the existing value
        METRICS mergedValue = merge(existingValue, data);

        // Update the cache with the merged value
        cache.put(data.getKey(), mergedValue);
    }
}
}
