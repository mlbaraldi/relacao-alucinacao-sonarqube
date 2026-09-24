package generated;
public class Generated0d8a7a5cd0af {
public int appendLoopOnAppenders(LoggingEvent event){
    if (appenders != null) {
        for (Appender appender : appenders) {
            appender.doAppend(event);
        }
        return appenders.size(); // Return the number of appenders called
    }
    return 0; // Return 0 if no appenders are attached
}
}
