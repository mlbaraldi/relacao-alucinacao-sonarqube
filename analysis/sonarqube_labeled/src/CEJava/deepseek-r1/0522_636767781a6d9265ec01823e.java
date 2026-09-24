package generated;
public class Generatedc313f254af57 {
protected void append(LoggingEvent event){
    // Extract the formatted message from the logging event
    String message = event.getRenderedMessage() + "\n";
    byte[] messageBytes = message.getBytes(); // Uses default charset; consider specifying UTF-8 if needed

    // Synchronize access to the connectedClients list to ensure thread safety
    synchronized (connectedClients) {
        Iterator<OutputStream> iterator = connectedClients.iterator();
        while (iterator.hasNext()) {
            OutputStream stream = iterator.next();
            try {
                // Write the message bytes to the client's output stream and flush
                stream.write(messageBytes);
                stream.flush();
            } catch (IOException e) {
                // Remove the client if an exception occurs (e.g., disconnected)
                iterator.remove();
            }
        }
    }
}
}
