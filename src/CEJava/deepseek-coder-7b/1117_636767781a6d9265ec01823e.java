package generated;
public class Generatedc313f254af57 {
protected void append(LoggingEvent event){
    String message = event.getRenderedMessage();
    for (Client client : clients) {
        client.receiveMessage(message);
    }
}
}
