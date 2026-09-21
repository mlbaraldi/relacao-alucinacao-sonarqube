package generated;
public class Generatedcfd5238dc3c4 {
private String unescapeId(String input){
    if (input.length() < 2 || input.charAt(0) != '\'' || input.charAt(input.length() - 1) != '\'') {
        throw new IllegalArgumentException("Invalid input: " + input);
    }
    return input.substring(1, input.length() - 1);
}
}
