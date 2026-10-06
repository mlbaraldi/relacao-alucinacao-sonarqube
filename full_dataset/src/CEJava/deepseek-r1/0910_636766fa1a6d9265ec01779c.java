package generated;
public class Generated92c2f872761e {
private String parseToken(final char[] terminators){
    StringBuilder token = new StringBuilder();
    while (pos < input.length) {
        char current = input[pos];
        boolean isTerminator = false;
        for (char term : terminators) {
            if (current == term) {
                isTerminator = true;
                break;
            }
        }
        if (isTerminator) {
            break;
        }
        token.append(current);
        pos++;
    }
    return token.toString();
}
}
