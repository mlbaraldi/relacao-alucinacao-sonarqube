package generated;
public class Generatedc313f254af57 {
protected void append(LoggingEvent event){
    for (Socket client : clients) {
        try {
            // Here you would need to write the message to the client.
            // For simplicity, let's just print the message to the console.
            System.out.println(event.getMessage());
        } catch (IOException e) {
            // Handle the exception if something goes wrong.
            e.printStackTrace();
        }
    }
}
}
