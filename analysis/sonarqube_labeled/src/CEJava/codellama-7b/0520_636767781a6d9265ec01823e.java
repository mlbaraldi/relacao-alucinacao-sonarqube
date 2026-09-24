package generated;
public class Generatedc313f254af57 {
protected void append(LoggingEvent event){
    // Get the message from the event
    String message = event.getMessage();

    // Get the list of connected clients
    List<Client> clients = getClients();

    // Iterate over the clients and write the message to each one
    for (Client client : clients) {
        client.write(message);
    }
}
}
