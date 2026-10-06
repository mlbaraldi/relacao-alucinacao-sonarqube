package generated;
public class Generatedcfd5238dc3c4 {
private String unescapeId(String input){
    if (input == null) {
        return null;
    }
    return input.replace("\\\\", "\\")
                 .replace("\\\"", "\"")
                 .replace("\\n", "\n")
                 .replace("\\r", "\r")
                 .replace("\\t", "\t");
}
}
