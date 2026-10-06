package generated;
public class Generated7ec8ff8b15b2 {
public static String encodeTemplateNames(String s){
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '{' || c == '}') {
            sb.append('%');
            sb.append(Integer.toHexString(c));
        } else {
            sb.append(c);
        }
    }
    return sb.toString();
}
}
