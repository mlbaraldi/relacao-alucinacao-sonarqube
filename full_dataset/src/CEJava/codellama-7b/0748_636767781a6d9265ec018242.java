package generated;
public class Generated0d8a7a5cd0af {
public int appendLoopOnAppenders(LoggingEvent event){
    int numAppended = 0;
    for (Appender appender : appenders) {
        numAppended += appender.doAppend(event);
    }
    return numAppended;
}
}
