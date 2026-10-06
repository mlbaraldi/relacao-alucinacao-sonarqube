package generated;
public class Generated08e6377ff6e0 {
public int decide(LoggingEvent event){
    // Check if the message object is a string
    if (event.getMessage() instanceof String) {
        String message = event.getMessage().toString();

        // If the message contains a specific string, deny it
        if (message.contains("YourString")) {
            return Filter.DENY;
        }
    }

    // If there is no match, return neutral
    return Filter.NEUTRAL;
}
}
