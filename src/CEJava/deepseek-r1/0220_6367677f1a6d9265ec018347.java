package generated;
public class Generated9b1651bbf862 {
public synchronized void send(final String message){
    String telnetMessage = message + "\r\n";
    Iterator<Client> iterator = clients.iterator();
    while (iterator.hasNext()) {
        Client client = iterator.next();
        try {
            OutputStream output = client.getOutputStream();
            output.write(telnetMessage.getBytes());
            output.flush();
        } catch (IOException e) {
            iterator.remove();
            try {
                client.close();
            } catch (IOException ex) {
                // Log or handle the exception if needed
            }
        }
    }
}
}
