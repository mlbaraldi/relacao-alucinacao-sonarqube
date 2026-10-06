package generated;
public class Generatedb8d840f5aa02 {
public Boolean isPartialContentResponse(){
    try {
        URL url = new URL("http://example.com"); // replace with your URL
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        int responseCode = connection.getResponseCode();
        connection.disconnect();
        return responseCode == HttpURLConnection.HTTP_PARTIAL;
    } catch (Exception e) {
        e.printStackTrace();
        return false;
    }
}
}
