package generated;
public class Generated567fd55140de {
public static String unescapeJava(String str) throws Exception {
    if (str == null) {
        return null;
    }

    StringBuilder unescaped = new StringBuilder();
    boolean escape = false;

    for (char c : str.toCharArray()) {
        if (escape) {
            switch (c) {
                case 'n':
                    unescaped.append('\n');
                    break;
                case 't':
                    unescaped.append('\t');
                    break;
                case 'r':
                    unescaped.append('\r');
                    break;
                case '\"':
                    unescaped.append('\"');
                    break;
                case '\'':
                    unescaped.append('\'');
                    break;
                case '\\':
                    unescaped.append('\\');
                    break;
                default:
                    throw new Exception("Invalid escape character: " + c);
            }
            escape = false;
        } else if (c == '\\') {
            escape = true;
        } else {
            unescaped.append(c);
        }
    }

    return unescaped.toString();
}
}
