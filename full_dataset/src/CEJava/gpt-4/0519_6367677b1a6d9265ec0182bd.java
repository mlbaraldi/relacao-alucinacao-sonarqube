package generated;
public class Generated601f27adee4b {
public String format(final LoggingEvent event){
    StringBuilder sb = new StringBuilder();

    // Append timestamp
    sb.append(event.getTimestamp());
    sb.append(" - ");

    // Append level
    sb.append(event.getLevel());
    sb.append(" - ");

    // Append logger name
    sb.append(event.getLoggerName());
    sb.append(" - ");

    // Append message
    sb.append(event.getMessage());

    return sb.toString();
}
}
