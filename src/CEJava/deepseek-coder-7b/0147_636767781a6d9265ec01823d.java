package generated;
public class Generated10b3e2f27a4d {
protected void subAppend(LoggingEvent event){
    String logMessage = event.getLevel() + ": " + event.getMessage();
    fileManager.writeToFile(logMessage);
}
}
