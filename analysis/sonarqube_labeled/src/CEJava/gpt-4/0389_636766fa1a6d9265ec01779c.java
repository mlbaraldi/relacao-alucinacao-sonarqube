package generated;
public class Generated92c2f872761e {
private String parseToken(final char[] terminators){
    StringBuilder token = new StringBuilder();
    while (position < source.length()) {
        char currentChar = source.charAt(position);
        for (char terminator : terminators) {
            if (currentChar == terminator) {
                position++; // Move past the terminator
                return token.toString();
            }
        }
        token.append(currentChar);
        position++;
    }
    return token.toString(); // Return the token even if no terminator was found
}
}
