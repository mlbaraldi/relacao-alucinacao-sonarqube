package generated;
public class Generated7746ec4e0a66 {
public ByteVector putInt(final int intValue){
    byte[] bytes = new byte[4];
    bytes[0] = (byte)((intValue >> 24) & 0xFF);
    bytes[1] = (byte)((intValue >> 16) & 0xFF);
    bytes[2] = (byte)((intValue >> 8) & 0xFF);
    bytes[3] = (byte)(intValue & 0xFF);
    return new ByteVector(bytes);
}
}
