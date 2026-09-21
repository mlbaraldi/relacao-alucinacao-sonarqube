package generated;
public class Generatedf97fda04fd1b {
public void add(LoggingEvent event){
    // Check if the buffer is full
    if (buffer.size() >= maxSize) {
        // If the buffer is full, remove the oldest event
        buffer.remove(0);
    }
    // Add the new event to the end of the buffer
    buffer.add(event);
}
}
