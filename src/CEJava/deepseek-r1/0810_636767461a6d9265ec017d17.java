package generated;
public class Generatedcfd5238dc3c4 {
private String unescapeId(String input){
    StringBuilder sb = new StringBuilder();
    int length = input.length();
    int i = 0;
    while (i < length) {
        char c = input.charAt(i);
        if (c == '\\' && i + 1 < length) {
            char next = input.charAt(i + 1);
            if (next == '"' || next == '\\') {
                sb.append(next);
                i += 2;
            } else {
                sb.append(c);
                sb.append(next);
                i += 2;
            }
        } else {
            sb.append(c);
            i += 1;
        }
    }
    return sb.toString();
}
}
