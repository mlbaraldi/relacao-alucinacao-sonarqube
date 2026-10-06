package generated;
public class Generatedaf336a6bf556 {
public static String base64Decode(final String s){
    // Decode the Base64 encoded string
    byte[] decodedBytes = Base64.getDecoder().decode(s);
    
    // Convert the decoded bytes to a string
    String decodedString = new String(decodedBytes);
    
    return decodedString;
}
}
