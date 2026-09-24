package generated;
public class Generated0d8a7a5cd0af {
public int appendLoopOnAppenders(LoggingEvent event){
    if (appenders == null || appenders.isEmpty()) {
        return 0;
    }
    int count = 0;
    for (Appender appender : appenders) {
        appender.doAppend(event);
        count++;
    }
    return count;
}
}
