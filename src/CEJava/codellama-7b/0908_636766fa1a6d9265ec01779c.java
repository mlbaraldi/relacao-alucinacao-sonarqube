package generated;
public class Generated92c2f872761e {
private String parseToken(final char[] terminators){
    StringBuilder token = new StringBuilder();
    boolean isToken = false;

    for (char c : input) {
        if (isToken) {
            token.append(c);
        } else if (terminators.contains(c)) {
            break;
        } else {
            isToken = true;
            token.append(c);
        }
    }

    return token.toString();
}
}
