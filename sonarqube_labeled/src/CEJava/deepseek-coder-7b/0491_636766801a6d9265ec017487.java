package generated;
public class Generated7ec8ff8b15b2 {
public static String encodeTemplateNames(String s){
    if(s == null || s.length() == 0) {
        return s;
    }

    StringBuilder sb = new StringBuilder();
    for(char c : s.toCharArray()) {
        if(c == '{' || c == '}') {
            sb.append("%");
            sb.append(Integer.toHexString(c));
        } else {
            sb.append(c);
        }
    }

    return sb.toString();
}
}
