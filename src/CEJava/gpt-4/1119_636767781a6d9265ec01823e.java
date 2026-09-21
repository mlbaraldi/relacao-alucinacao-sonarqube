package generated;
public class Generatedc313f254af57 {
protected void append(LoggingEvent event){
    String message = event.getMessage().toString();

    for (Socket client : clients) {
        try {
            PrintWriter out = new PrintWriter(client.getOutputStream(), true);
            out.println(message);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
}
