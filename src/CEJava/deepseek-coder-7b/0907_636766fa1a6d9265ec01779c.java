package generated;
public class Generated92c2f872761e {
private String parseToken(final char[] terminators){
    StringBuilder token = new StringBuilder();
    boolean isTerminatorFound = false;

    while (!isTerminatorFound && input.hasMoreTokens()){
        char currentChar = input.nextToken();
        token.append(currentChar);

        for (char terminator : terminators){
            if (currentChar == terminator){
                isTerminatorFound = true;
                break;
            }
        }
    }

    return token.toString();
}
}
