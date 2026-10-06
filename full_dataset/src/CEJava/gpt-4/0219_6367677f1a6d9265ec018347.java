package generated;
public class Generated9b1651bbf862 {
public synchronized void send(final String message){
    for (Socket client : clients) {
        try {
            PrintWriter out = new PrintWriter(client.getOutputStream(), true);
            out.println(message);
        } catch (Exception e) {
            System.out.println("Error sending message to client: " + e.getMessage());
        }
    }
}
}
