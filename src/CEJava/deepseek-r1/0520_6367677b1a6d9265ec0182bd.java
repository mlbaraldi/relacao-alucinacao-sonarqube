package generated;
public class Generated601f27adee4b {
public String format(final LoggingEvent event){
    // Format the timestamp
    Date date = new Date(event.getTimeStamp());
    SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS");
    String formattedDate = sdf.format(date);
    
    // Get log level, logger name, thread name, and message
    String level = event.getLevel().toString();
    String loggerName = event.getLoggerName();
    String threadName = event.getThreadName();
    String message = event.getRenderedMessage();
    
    // Handle null message
    if (message == null) {
        message = "";
    }
    
    // Build the formatted string
    StringBuilder sb = new StringBuilder();
    sb.append(String.format("[%s] [%s] [%s] [%s] - %s",
            formattedDate, level, loggerName, threadName, message));
    
    // Append throwable stack trace if present
    ThrowableInformation throwableInfo = event.getThrowableInformation();
    if (throwableInfo != null) {
        Throwable throwable = throwableInfo.getThrowable();
        String stackTrace = getStackTrace(throwable);
        sb.append("\n").append(stackTrace);
    }
    
    return sb.toString();
}
}
