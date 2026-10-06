package generated;
public class Generated08e6377ff6e0 {
public int decide(LoggingEvent event){
    String message = event.getMessage();
    if (message.contains("string match")) {
        return Filter.NEUTRAL;
    }
    return Filter.DENY;
}
}
