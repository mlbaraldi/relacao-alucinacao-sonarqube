package generated;
public class Generated601f27adee4b {
public String format(final LoggingEvent event){
    Logger logger = Logger.getLogger(this.getClass());
    String format = "Event [Priority: %s, Timestamp: %s, Source: %s, Message: %s]";
    return String.format(format, event.getLevel().toString(), event.getTimeStamp(), event.getSource().toString(), event.getRenderedMessage());
}
}
