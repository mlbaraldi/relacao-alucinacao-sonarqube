package generated;
public class Generated567fd55140de {
public static String unescapeJava(String str) throws Exception {
    if (str == null) {
        return null;
    }
    int sz = str.length();
    StringBuilder sb = new StringBuilder(sz);
    int i = 0;
    while (i < sz) {
        char ch = str.charAt(i);
        if (ch == '\\') {
            if (i == sz - 1) {
                sb.append(ch);
                break;
            }
            char next = str.charAt(i + 1);
            switch (next) {
                case '\\':
                    sb.append('\\');
                    i += 2;
                    break;
                case 'b':
                    sb.append('\b');
                    i += 2;
                    break;
                case 't':
                    sb.append('\t');
                    i += 2;
                    break;
                case 'n':
                    sb.append('\n');
                    i += 2;
                    break;
                case 'f':
                    sb.append('\f');
                    i += 2;
                    break;
                case 'r':
                    sb.append('\r');
                    i += 2;
                    break;
                case '\"':
                    sb.append('"');
                    i += 2;
                    break;
                case '\'':
                    sb.append('\'');
                    i += 2;
                    break;
                case 'u':
                    if (i + 5 >= sz) {
                        throw new Exception("Incomplete Unicode escape sequence at index " + i);
                    }
                    String hexDigits = str.substring(i + 2, i + 6);
                    try {
                        int codePoint = Integer.parseInt(hexDigits, 16);
                        sb.append((char) codePoint);
                        i += 6;
                    } catch (NumberFormatException e) {
                        throw new Exception("Invalid Unicode escape: " + hexDigits, e);
                    }
                    break;
                case '0':
                case '1':
                case '2':
                case '3':
                case '4':
                case '5':
                case '6':
                case '7':
                    int octalEnd = i + 1;
                    int octalDigits = 1;
                    while (octalDigits < 3 && octalEnd + 1 < sz) {
                        char octalChar = str.charAt(octalEnd + 1);
                        if (octalChar >= '0' && octalChar <= '7') {
                            octalEnd++;
                            octalDigits++;
                        } else {
                            break;
                        }
                    }
                    String octalStr = str.substring(i + 1, octalEnd + 1);
                    try {
                        int value = Integer.parseInt(octalStr, 8);
                        if (value > 0xFF) {
                            throw new Exception("Octal escape sequence exceeds 377: \\" + octalStr);
                        }
                        sb.append((char) value);
                        i = octalEnd + 1;
                    } catch (NumberFormatException e) {
                        throw new Exception("Invalid octal escape sequence: \\" + octalStr, e);
                    }
                    break;
                default:
                    throw new Exception("Invalid escape sequence: \\" + next + " at index " + i);
            }
        } else {
            sb.append(ch);
            i++;
        }
    }
    return sb.toString();
}
}
