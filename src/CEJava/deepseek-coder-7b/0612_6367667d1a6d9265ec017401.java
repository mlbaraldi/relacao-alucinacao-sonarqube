package generated;
public class Generated567fd55140de {
public static String unescapeJava(String str) throws Exception {
    if (str == null) {
        return null;
    }

    StringBuilder sb = new StringBuilder(str.length());
    for (int i = 0; i < str.length(); i++) {
        char c = str.charAt(i);
        if (c == '\\') {
            if (i + 1 < str.length()) {
                char nextChar = str.charAt(i + 1);
                switch (nextChar) {
                    case 'n':
                        sb.append('\n');
                        i++; // Skip the next character
                        break;
                    case 't':
                        sb.append('\t');
                        i++; // Skip the next character
                        break;
                    case '\\':
                        sb.append('\\');
                        i++; // Skip the next character
                        break;
                    default:
                        sb.append(c); // Append the backslash
                        break;
                }
            } else {
                sb.append(c); // Append the backslash
            }
        } else {
            sb.append(c);
        }
    }

    return sb.toString();
}
}
