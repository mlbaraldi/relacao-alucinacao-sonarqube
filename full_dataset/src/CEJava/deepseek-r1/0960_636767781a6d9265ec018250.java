package generated;
public class Generated08e6377ff6e0 {
public int decide(LoggingEvent event){
    String message = event.getRenderedMessage();
    // Assuming 'stringToMatch' is a class member variable holding the target string
    if (message != null && message.contains(stringToMatch)) {
        return Filter.ACCEPT; // Or another appropriate decision
    }
    return Filter.NEUTRAL;
}
}
