package generated;
public class Generated0d8a7a5cd0af {
public int appendLoopOnAppenders(LoggingEvent event){
    for (Appender appender : appenders) {
        appender.doAppend(event);
    }
    return appenders.size();
}
}
