package generated;
public class Generated74eaaf0a8040 {
private static String javaCharset(String charset){
    try {
        return java.nio.charset.Charset.forName(charset).name();
    } catch (Exception e) {
        return null;
    }
}
}
