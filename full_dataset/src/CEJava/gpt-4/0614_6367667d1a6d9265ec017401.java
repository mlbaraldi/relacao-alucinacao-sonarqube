package generated;
public class Generated567fd55140de {
public static String unescapeJava(String str) throws Exception {
    if (str == null) {
        return null;
    }
    StringBuilder newStr = new StringBuilder(str.length());
    for (int i = 0; i < str.length(); i++) {
        char ch = str.charAt(i);
        if (ch == '\\' && i < str.length() - 1) {
            char nextChar = str.charAt(i + 1);
            switch (nextChar) {
                case 'n':
                    newStr.append('\n');
                    i++;
                    break;
                case 't':
                    newStr.append('\t');
                    i++;
                    break;
                case 'b':
                    newStr.append('\b');
                    i++;
                    break;
                case 'r':
                    newStr.append('\r');
                    i++;
                    break;
                case 'f':
                    newStr.append('\f');
                    i++;
                    break;
                case '\'':
                    newStr.append('\'');
                    i++;
                    break;
                case '\"':
                    newStr.append('\"');
                    i++;
                    break;
                case '\\':
                    newStr.append('\\');
                    i++;
                    break;
                default:
                    newStr.append(ch);
                    break;
            }
        } else {
            newStr.append(ch);
        }
    }
    return newStr.toString();
}
}
