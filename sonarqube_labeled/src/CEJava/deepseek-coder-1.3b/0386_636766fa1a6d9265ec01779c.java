package generated;
public class Generated92c2f872761e {
private String parseToken(final char[] terminators){
    StringBuilder token = new StringBuilder();
    boolean foundTerminator = false;

    for (char c : terminators) {
        if (foundTerminator) {
            break;
        }

        // Check if the current character is a terminator
        for (char terminator : terminators) {
            if (c == terminator) {
                foundTerminator = true;
                break;
            }
        }

        if (!foundTerminator) {
            token.append(c);
        }
    }

    return token.toString();
}
}
