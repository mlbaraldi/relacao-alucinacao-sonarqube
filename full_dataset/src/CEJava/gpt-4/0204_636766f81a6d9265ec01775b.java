package generated;
public class Generated157f4a2d9370 {
public long readLong(final int offset){
    long result = 0;
    for (int i = 0; i < 8; i++) {
        result <<= 8;
        result |= (b[offset + i] & 0xFF);
    }
    return result;
}
}
