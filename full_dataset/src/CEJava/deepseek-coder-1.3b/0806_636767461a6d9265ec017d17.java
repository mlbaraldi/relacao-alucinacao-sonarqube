package generated;
public class Generatedcfd5238dc3c4 {
private String unescapeId(String input){
    StringBuilder output = new StringBuilder();
    for (char c : input.toCharArray()) {
        if (c == '\\') {
            output.append(input.charAt(++i));
        } else {
            output.append(c);
        }
    }
    return output.toString();
}
}
