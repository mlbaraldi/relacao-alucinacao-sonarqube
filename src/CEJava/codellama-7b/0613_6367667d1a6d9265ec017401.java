package generated;
public class Generated567fd55140de {
public static String unescapeJava(String str) throws Exception {
    if (str == null) {
        return null;
    }

    StringBuilder sb = new StringBuilder(str.length());
    boolean escaped = false;
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if (escaped) {
            switch (c) {
                case 'n':
                    sb.append('\n');
                    break;
                case 'r':
                    sb.append('\r');
                    break;
                case 't':
                    sb.append('\t');
                    break;
                case 'b':
                    sb.append('\b');
                    break;
                case 'f':
                    sb.append('\f');
                    break;
                case '\'':
                    sb.append('\'');
                    break;
                case '\"':
                    sb.append('\"');
                    break;
                case '\\':
                    sb.append('\\');
                    break;
                default:
                    throw new Exception("Invalid escape sequence: \\" + c);
            }
            escaped = false;
        } else if (c == '\\') {
            escaped = true;
        } else {
            sb.append(c);
        }
    }

    return sb.toString();
}
}
