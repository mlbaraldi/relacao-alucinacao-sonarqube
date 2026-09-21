package generated;
public class Generated9b1651bbf862 {
public synchronized void send(final String message){
    for (Client client : clients) {
        client.send(message);
    }
}
}
