package generated;
public class Generated157f4a2d9370 {
public long readLong(final int offset){
    long value = 0;
    for (int i = 0; i < 8; i++) {
        value = (value << 8) | (bytes[offset + i] & 0xFF);
    }
    return value;
}
}
