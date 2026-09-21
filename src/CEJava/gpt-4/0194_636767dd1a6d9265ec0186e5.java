package generated;
public class Generated24c200d6ae7f {
public void addNewTarget(Channels channels,IConsumer consumer){
    // Check if the consumer is already in the map
    if (consumerChannels.containsKey(consumer)) {
        // If the consumer is already in the map, add the new channel to their list of channels
        consumerChannels.get(consumer).add(channels);
    } else {
        // If the consumer is not in the map, create a new list of channels for them
        List<Channels> channelsList = new ArrayList<>();
        channelsList.add(channels);
        consumerChannels.put(consumer, channelsList);
    }
}
}
