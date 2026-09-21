package generated;
public class Generateda70133497692 {
public static LinkedBuffer writeUTF8(final CharSequence str,final WriteSession session,final LinkedBuffer lb){
    byte[] bytes = str.toString().getBytes(StandardCharsets.UTF_8);
    lb.write(bytes);
    return lb;
}
}
