package generated;
public class Generated7ec8ff8b15b2 {
public static String encodeTemplateNames(String s){
    if(s == null) {
        return null;
    }
    return s.replace("{", "%7B").replace("}", "%7D");
}
}
