package generated;
public class Generated7ec8ff8b15b2 {
public static String encodeTemplateNames(String s){
    if (s == null) {
        return null;
    }
    StringBuilder sb = new StringBuilder();
    for (char c : s.toCharArray()) {
        if (c == '{') {
            sb.append("%7B");
        } else if (c == '}') {
            sb.append("%7D");
        } else {
            sb.append(c);
        }
    }
    return sb.toString();
}
}
