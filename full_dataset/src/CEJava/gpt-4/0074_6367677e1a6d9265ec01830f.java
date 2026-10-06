package generated;
public class Generated681daa0a9066 {
public String format(LoggingEvent event){
    StringBuilder sb = new StringBuilder();

    // Append the logger name
    sb.append(event.getLoggerName());
    sb.append(" - ");

    // Append the level of the log
    sb.append(event.getLevel());
    sb.append(": ");

    // Append the message of the log
    sb.append(event.getMessage());

    // Append the timestamp of the log
    sb.append(" [at ");
    sb.append(event.getTimeStamp());
    sb.append("]");

    // Append the thread name of the log
    sb.append(" <in ");
    sb.append(event.getThreadName());
    sb.append(">");

    return sb.toString();
}
}
