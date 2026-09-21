package generated;
public class Generated681daa0a9066 {
public String format(LoggingEvent event){
    String pattern = event.getPattern();
    String message = event.getMessage();
    String level = event.getLevel().toString();
    String logger = event.getLoggerName();
    String thread = event.getThreadName();
    String time = event.getTimeStamp().toString();

    // Replace placeholders in the pattern with the corresponding values
    pattern = pattern.replace("{message}", message);
    pattern = pattern.replace("{level}", level);
    pattern = pattern.replace("{logger}", logger);
    pattern = pattern.replace("{thread}", thread);
    pattern = pattern.replace("{time}", time);

    return pattern;
}
}
