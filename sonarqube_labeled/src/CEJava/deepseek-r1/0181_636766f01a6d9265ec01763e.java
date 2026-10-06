package generated;
public class Generated74eaaf0a8040 {
private static String javaCharset(String charset){
    try {
        return Charset.forName(charset).name();
    } catch (IllegalCharsetNameException | UnsupportedCharsetException e) {
        return charset;
    }
}
}
