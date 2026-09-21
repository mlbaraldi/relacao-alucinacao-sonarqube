package generated;
public class Generated10b3e2f27a4d {
protected void subAppend(LoggingEvent event){
    try {
        writer.write(event.getRenderedMessage());
        writer.newLine();
        writer.flush();
    } catch (IOException e) {
        System.out.println("An error occurred while writing to the log file: " + e.getMessage());
    }
}
}
