package generated;
public class Generated10b3e2f27a4d {
protected void subAppend(LoggingEvent event){
    // Get the log message and its level
    String message = event.getMessage();
    Level level = event.getLevel();

    // Check if the log message is at the desired level
    if (level.equals(Level.INFO)) {
        // Write the log message to the console
        System.out.println(message);
    }
}
}
