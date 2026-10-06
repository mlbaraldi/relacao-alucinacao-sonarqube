package generated;
public class Generated71b03dbc71b6 {
@Override public void accept(final METRICS data){
    String id = data.getId(); // Assuming METRICS has a method getId() to get unique identifier
    if (cache.containsKey(id)) {
        METRICS existingData = cache.get(id);
        existingData.merge(data); // Assuming METRICS has a method merge() to merge data
    } else {
        cache.put(id, data);
    }
}
}
