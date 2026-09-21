package generated;
public class Generatedc486c51583fa {
public final byte[] toByteArray(){
    int total = 0;
    for (byte[] buffer : buffers) {
        total += buffer.length;
    }
    byte[] result = new byte[total];
    int offset = 0;
    for (byte[] buffer : buffers) {
        System.arraycopy(buffer, 0, result, offset, buffer.length);
        offset += buffer.length;
    }
    return result;
}
}
