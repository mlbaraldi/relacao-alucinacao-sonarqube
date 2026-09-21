package generated;
public class Generateda70133497692 {
public static LinkedBuffer writeUTF8(final CharSequence str,final WriteSession session,final LinkedBuffer lb){
    // Convert the CharSequence to a String and get its bytes in UTF-8
    byte[] utf8Bytes = str.toString().getBytes(Charset.forName("UTF-8"));

    // Write the bytes into the LinkedBuffer
    for (byte b : utf8Bytes) {
        lb.writeByte(b, session);
    }

    return lb;
}
}
