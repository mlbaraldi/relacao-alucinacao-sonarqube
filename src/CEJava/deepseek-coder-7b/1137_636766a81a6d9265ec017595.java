package generated;
public class Generatedb94f6096aa70 {
final ByteVector put11(final int byteValue1,final int byteValue2){
    if (size >= bytes.length) {
        byte[] newBytes = new byte[bytes.length * 2];
        System.arraycopy(bytes, 0, newBytes, 0, bytes.length);
        bytes = newBytes;
    }

    bytes[size++] = (byte) byteValue1;
    bytes[size++] = (byte) byteValue2;

    return this;
}
}
